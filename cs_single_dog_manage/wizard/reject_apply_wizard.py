'''
@Author: your name
@Date: 2020-04-12 20:56:38
@LastEditTime: 2020-04-12 21:10:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/wizard/reject_apply_wizard.py
'''
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class RejectApplyWizard(models.TransientModel):
    _name = "reject.apply.wizard"
    _description = "Reject Apply Wizard"

    pair_apply_id = fields.Many2one('pair.apply', string='配对申请')

    reject_reason = fields.Char(string='拒绝原因')

    @api.model
    def default_get(self, fields_list):
        res = super(RejectApplyWizard, self).default_get(fields_list)
        res['pair_apply_id'] = self._context.get('active_id', False)
        return res

    def action_reject_apply(self):
        """
        拒绝配对申请
        """
        pair_apply_id = self.pair_apply_id
        reject_reason = self.reject_reason
        if pair_apply_id:
            pair_apply_id.write({
                'state': 'reject', 
                'reject_reason': reject_reason
                })