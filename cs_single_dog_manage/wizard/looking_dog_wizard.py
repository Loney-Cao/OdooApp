'''
@Author: your name
@Date: 2020-04-12 17:01:09
@LastEditTime: 2020-04-12 17:49:06
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/wizard/looking_dog_wizard.py
'''
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class LookingDogWizard(models.TransientModel):
    _name = "looking.dog.wizard"
    _description = "Looking Dog Wizard"

    dog_id = fields.Many2one('single.dog', string='单身狗')

    apply_dog_ids = fields.Many2many('single.dog', string='申请对象')
    apply_content = fields.Char(string='申请内容')


    @api.model
    def default_get(self, fields_list):
        res = super(LookingDogWizard, self).default_get(fields_list)
        res['dog_id'] = self._context.get('active_id', False)
        return res

    def action_apply(self):
        """"""
        dog_id = self.dog_id
        apply_dog_ids = self.apply_dog_ids
        if dog_id and apply_dog_ids:
            dog_id = self.dog_id
            vals = [{
                'send_dog_id':dog_id.id, 
                'recieved_dog_id': apply_dog_id.id, 
                'apply_content':self.apply_content
                } for apply_dog_id in apply_dog_ids]
            self.env['pair.apply'].create(vals)