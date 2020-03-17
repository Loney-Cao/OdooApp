# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Author： LoneyCao
# Blog： https://loneycao.gitee.io/
# Desc： 导出xml文件

from odoo import api, fields, models, _
import os
from .xml_tool import XmlTool

FILE_PATH = os.path.join(os.path.dirname(__file__), '../static/export/export.xml')


class ExportXmlWizard(models.TransientModel):
    _name = "export.xml.wizard"
    _description = "Export Xml Wizard"

    file_name = fields.Char('Download File Name', required=True)
    model = fields.Char('Model')
    field_ids = fields.Many2many('ir.model.fields', string="Don't Export Field")
    noupdate = fields.Boolean(string='Is Noupdate')

    def generate_xml(self, record, field_list=None):
        """
        生成记录的xml
        :param record:  记录
        :param field_list:  黑名单
        :return:
        """
        model = record._name
        record_id = model.replace('.', '_') + '_' + str(record.id)

        field_xml = """
            <record id="%s" model="%s" >""" % (record_id, model)
        for field, field_value in record.read()[0].items():
            if field in field_list:
                continue
            name = field
            value = field_value
            field_type = record._fields[field].type
            # model = record._fields[field].comodel_name
            if field_type == 'many2one':
                # record = self.env[model].search([('id', '=', field_value[1])])
                value = field_value[0] if field_value else False
                # self.generate_xml(record)
            elif field_type == 'one2many':
                value = [6, 0, field_value]
            elif field_type == 'many2many':
                value = [6, 0, field_value]
            field_xml += """
                <field name="%s">%s</field>""" % (name, str(value))
        record_xml = field_xml + """
            </record>\n"""
        return record_xml

    @api.model
    def export_xml(self, field_list=None, noupdate='0'):
        """
        导出xml文件
        :param field_list:
        :param noupdate:
        :return:
        """
        model = self._context.get('active_model')
        ids = self._context.get('active_ids')
        records = self.env[model].search([('id', 'in', ids)])

        # 以下代码注释，使用xml_tool生成xml文件， 效果一样

#         xml = """
# <?xml version="1.0" encoding="utf-8"?>
# <odoo>
#     <data noupdate="%d">
#         """ % int(noupdate)
#         for record in records:
#             xml += self.generate_xml(record, field_list)
#         xml += """
#     </data>
# </odoo>"""
#
#         with open(FILE_PATH, 'w') as f:
#             f.write(xml)

        xml_tool = XmlTool(FILE_PATH)
        xml_tool.generate_xml(records, field_list, noupdate)

    def download_file(self):
        """
        下载文件
        :return:
        """
        model = self._context.get('active_model')
        field_list = self.field_ids.mapped('name')
        noupdate = self.noupdate
        self.export_xml(field_list, str(int(noupdate)))
        file_name = self.file_name or model.replace('.', ' ').title()
        return {
            'type': 'ir.actions.act_url',
            'url': '/cs_export_xml/download_xml_file/file_name=%s.xml' % file_name,
            'target': 'self',
        }

    def open_export_xml_wizard(self):
        """
        打开配置向导
        :return:
        """
        return {
            'name': _('Export Xml Config'),
            'context': self.env.context,
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'export.xml.wizard',
            'type': 'ir.actions.act_window',
            'target': 'new'
        }

    @api.model
    def default_get(self, fields_list):
        res = super(ExportXmlWizard, self).default_get(fields_list)
        model = self._context.get('active_model')
        if model:
            res['model'] = model
            res['file_name'] = model.replace('.', ' ').title()
        return res
