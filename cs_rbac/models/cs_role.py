# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CsRole(models.Model):
    """用户角色模型"""

    _name = 'cs.role'
    _description = "Users Role"

    name = fields.Char(string='name', required=True)
    group_id = fields.Many2one('res.groups', string='Users Group')
    is_enable = fields.Boolean(string='Is Enable', default=True)
    user_ids = fields.One2many('res.users', 'cs_role_id', string='Users')
    menu_access_control_ids = fields.One2many('cs.menu.access.control', 'cs_role_id', string='Menu Access Control')



