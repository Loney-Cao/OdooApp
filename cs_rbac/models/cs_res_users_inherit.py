# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CsResUsers(models.Model):
    """用户模型"""

    _inherit= 'res.users'

    cs_role_id = fields.Many2one('cs.role', 'Role')


