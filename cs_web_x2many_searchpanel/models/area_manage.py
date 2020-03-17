# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AreaManage(models.Model):
    _name = 'area.manage'
    _description = '区域管理'

    name = fields.Char('管理者')
    position = fields.Char(string='职务')

    area_line = fields.One2many('area', 'manage_id', '上级区域')
