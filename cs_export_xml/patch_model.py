# -*- coding: utf-8 -*-
# Author： LoneyCao
# Blog： https://loneycao.gitee.io/
# Desc： 对fields_view_get使用补丁，添加服务器动作。本来写好了js文件进行添加，失误将js删除了，就懒得再写了（😅）。

from odoo import api
from odoo.models import BaseModel

origin_fields_view_get = BaseModel.fields_view_get


@api.model
def patch_fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):

    result = origin_fields_view_get(self, view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    if toolbar:
        action_config = self.env.ref('cs_export_xml.action_server_export_xml_config').read()[0]
        action_now = self.env.ref('cs_export_xml.action_server_export_xml_now').read()[0]
        result['toolbar']['action'].append(action_config)
        result['toolbar']['action'].append(action_now)
    return result


BaseModel.fields_view_get = patch_fields_view_get



