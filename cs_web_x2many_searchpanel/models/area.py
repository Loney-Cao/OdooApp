# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Area(models.Model):
    _name = 'area'
    _description = '区域'

    # _parent_store = True

    name = fields.Char(string='区域名')
    code = fields.Char(string='区域编号')
    people_number = fields.Float(string='区域人数(万)')
    manage_id = fields.Many2one('area.manage', '管理者')

    parent_id = fields.Many2one('area', '上级区域')

    @api.model
    def load_views(self, views, options=None):
        print(views)
        # if self.env.context.get('base_model_name') == 'area.manage':
        #     views.append([False, 'search'])
        return super(Area, self).load_views(views, options)



