# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Author： LoneyCao
# Blog： https://loneycao.gitee.io/
# Desc： xml管理工具，用于生成xml文件

from xml.dom.minidom import Document


class XmlTool:

    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.doc = Document()
        self.odoo_node = self.doc.createElement('odoo')
        self.doc.appendChild(self.odoo_node)
        self.data_node = self.doc.createElement('data')

    def read_xml(self):
        """
        读取xml文件
        :return:
        """
        file = open(self.xml_path, 'rb').read()
        return file

    def get_xmlid(self, record, field):
        """
        获取关系字段对应记录的xmlid
        :param record: 当前模型记录
        :param field: 关系型字段
        :return: 返回xmlid列表
        """
        # 尝试获取xml_id
        rel_model = getattr(record, field)
        if rel_model:
            meta_data = rel_model.get_metadata()
            xmlid_list = [data.get('xmlid') for data in meta_data]
            return xmlid_list

    def generate_record_xml(self, records, field_list):
        """
        生成record记录的xml
        :param records:  记录集
        :param field_list:  字段黑名单
        :return:
        """
        doc = self.doc  # doc对象
        for record in records:  # 循环每个记录
            record_node = doc.createElement('record')  # 创建record节点
            model = record._name
            record_id = model.replace('.', '_') + '_' + str(record.id)  # 获取record节点属性
            record_node.setAttribute('id', record_id)
            record_node.setAttribute('model', model)

            for field, field_value in record.read()[0].items():  # 循环record的每个字段
                if field in field_list:  # 判断是否在黑名单
                    continue

                name = field  # 字段名
                value = field_value  # 字段值
                field_type = record._fields[field].type  # 字段类型

                field_node = doc.createElement('field')  # 创建field节点
                field_node.setAttribute('name', name)  # 设置name属性

                if field_type == 'many2one':  # m2o类型 尝试获取xmlid 使用ref属性， 否则直接使用值
                    # 尝试获取xml_id
                    xmlid = self.get_xmlid(record, field)
                    if xmlid:
                        field_node.setAttribute('ref', xmlid[0])
                        value = ''
                    else:
                        value = field_value[0] if field_value else False
                elif field_type == 'one2many':  # o2m类型 直接创建记录
                    rel_model_ids = getattr(record, field)
                    self.generate_record_xml(rel_model_ids, [])
                    continue
                elif field_type == 'many2many':  # m2m类型 同o2m类型
                    xmlid_list = self.get_xmlid(record, field)
                    if xmlid_list:
                        eval = [(6, 0, 'ref(%s)' % xmlid) for xmlid in xmlid_list]
                        field_node.setAttribute('eval', str(eval))
                        value = ''
                    else:
                        value = [6, 0, field_value[0] if field_value else False]

                value_node = doc.createTextNode(str(value))  # 创建字段值节点
                field_node.appendChild(value_node)  # 将字段值添加到field节点
                record_node.appendChild(field_node)  # 将field节点添加到record节点

            self.data_node.appendChild(record_node)  # 将record节点添加到data节点

    def generate_xml(self, records, field_list, noupdate):
        """
        生成xml文件
        :param records:  记录集
        :param field_list:  字段黑名单
        :param noupdate:  noupdate属性
        :return:
        """
        doc = self.doc
        self.data_node.setAttribute('noupdate', noupdate)  # 设置noupdate属性
        self.generate_record_xml(records, field_list)  # 生成data节点
        self.odoo_node.appendChild(self.data_node)  # 将data节点添加到odoo节点
        with open(self.xml_path, 'w') as f:  # 写入文件
            doc.writexml(f, indent='\t', newl='\n', addindent='\t')


if __name__ == "__main__":
    xml_tool = XmlTool("test.txt")
