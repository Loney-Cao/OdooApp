# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CsIrRule(models.Model):
    """记录规则模型"""

    _inherit= 'ir.rule'

    menu_access_control_id = fields.Many2one('cs.menu.access.control', string='Menu Access Control')


