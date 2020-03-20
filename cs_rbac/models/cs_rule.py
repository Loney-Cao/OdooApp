# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CsRule(models.Model):
    """规则模型"""

    _name = 'cs.rule'
    _description = "Rule"

    name = fields.Char(string='name', required=True)
    domain = fields.Char(string='Domain Force')

    menu_access_control_id = fields.Many2one('cs.menu.access.control', string='Menu Access Control')
    rule_id = fields.Many2one('ir.rule', string='Record Rules')



