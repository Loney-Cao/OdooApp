from odoo import api
from odoo.models import BaseModel

origin_fields_view_get = BaseModel.fields_view_get


@api.model
def patch_fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    print('\033[0;36m')
    print('*'*100)
    print('执行猴子补丁了')
    module = self.env['ir.module.module'].sudo().search([('name', '=', 'cs_export_xml')])
    if module:
        print(module, module.state)
    print('*'*100)
    print('\033[0m')
    result = origin_fields_view_get(self, view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    if toolbar and module.state == 'install':
        action_config = self.env.ref('cs_export_xml.action_server_export_xml_config').read()[0]
        action_now = self.env.ref('cs_export_xml.action_server_export_xml_now').read()[0]
        result['toolbar']['action'].append(action_config)
        result['toolbar']['action'].append(action_now)
    return result


def patch_fvg():

    BaseModel.fields_view_get = patch_fields_view_get
