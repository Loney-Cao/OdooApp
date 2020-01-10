# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Search(models.Model):

    _name = 'search'

    name = fields.Char(string='name')

    def get_models_data(self):
        models_data = [{'id': model['id'], 'text':model['name']} for model in self.env['ir.model'].search_read([], fields=['id', 'name'])]
        return models_data

    def get_search_data_html(self, model_id):
        print('*' * 100)
        model = self.env['ir.model'].search([('id', '=', model_id)], limit=1).model
        fields = self.env['ir.model.fields'].search([('model_id', '=', model_id)])
        field_dict = {field.name: field.field_description for field in fields}
        field_list = sorted(field_dict.items(), key=lambda item: item[0])

        records = self.env[model].search([])
        thead_html = '<thead><tr>'
        for field in field_list:
            thead_html += '<th>%s</th>' % field[1]
        thead_html += '</tr></thead>'
        tbody_html = '<tbody>'
        for rec in records:
            thead_html += '<tr>'
            for field in field_list:
                thead_html += '<th>%s</th>' % getattr(rec, field[0])
            thead_html += '</tr>'
        tbody_html += '</tbody>'
        html = thead_html + tbody_html
        return html

