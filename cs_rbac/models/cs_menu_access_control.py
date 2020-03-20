# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CsMenuAccessControl(models.Model):
    """菜单权限控制模型"""

    _name = 'cs.menu.access.control'
    _description = "Menu Access Control"

    cs_role_id = fields.Many2one('cs.role', string='Role')
    menu_id = fields.Many2one('ir.ui.menu', string='Menu', required=True, ondelete='cascade')
    menu_action = fields.Reference(selection=[('ir.actions.report', 'ir.actions.report'),
                                         ('ir.actions.act_window', 'ir.actions.act_window'),
                                         ('ir.actions.act_url', 'ir.actions.act_url'),
                                         ('ir.actions.server', 'ir.actions.server'),
                                         ('ir.actions.client', 'ir.actions.client')])
    menu_model = fields.Many2one('ir.model', string='Menu Model', ondelete='cascade')
    is_show_menu = fields.Boolean(string='Is Show Menu', default=True)
    perm_read = fields.Boolean(string='Read Access')
    perm_write = fields.Boolean(string='Write Access')
    perm_create = fields.Boolean(string='Create Access')
    perm_unlink = fields.Boolean(string='Delete Access')
    model_access_id = fields.Many2one('ir.model.access', string='Access Controls')

    cs_rule_ids = fields.One2many('cs.rule', 'menu_access_control_id', string='Rules')
    rule_ids = fields.One2many('ir.rule', 'model_id', string='Record Rules')



