'''
@Author: your name
@Date: 2020-04-12 14:20:13
@LastEditTime: 2020-04-12 23:12:25
@LastEditors: Please set LastEditors
@Description: 配对历史
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/models/pair_history.py
'''
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PairHistory(models.Model):
    _name = 'pair.history'
    _description = 'Pair History'  # 配对历史

    apply_id = fields.Many2one('pair.apply', ondelete='cascade', string='配对申请')

    dog_id = fields.Many2one('single.dog', ondelete='cascade', string='单身狗')
    # 交往对象
    pair_dog_id = fields.Many2one('single.dog', ondelete='cascade', string='对象')
    name = fields.Char(related='pair_dog_id.name', string='姓名')
    age = fields.Integer(related='pair_dog_id.age', string='年龄')
    gender = fields.Selection([
        ('man', '男'), 
        ('women', '女'), 
        ('unknow', '未知')], related='pair_dog_id.gender', string='性别')
    job = fields.Char(related='pair_dog_id.job', string='工作')

    # 交往结果
    state = fields.Selection([
        ('success', '成功'), 
        ('failed', '失败'), 
        ('pairing', '配对中')], string='结果', default='pairing')
    failed_reason = fields.Char(string='失败原因')


