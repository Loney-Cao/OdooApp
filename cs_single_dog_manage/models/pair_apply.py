'''
@Author: your name
@Date: 2020-04-12 14:18:30
@LastEditTime: 2020-04-12 23:16:01
@LastEditors: Please set LastEditors
@Description: 配对申请
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/models/pair_apply.py
'''
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class PairApply(models.Model):
    _name = 'pair.apply'
    _description = 'Pair Apply'  # 配对申请

    # 发出申请人
    send_dog_id = fields.Many2one('single.dog', ondelete='cascade', string='发出申请人')
    send_state = fields.Selection([
        ('waiting', '等待中'),
        ('looking', '寻找中'),
        ('pairing', '配对中'),
        ('pair_succese', '配对成功'),
        ('pair_failed', '配对失败')], related='send_dog_id.state', string='发出申请人状态')
    send_name = fields.Char(related='send_dog_id.name', string='申请人姓名')
    send_age = fields.Integer(related='send_dog_id.age', string='申请人年龄')
    send_gender = fields.Selection([
        ('man', '男'), 
        ('women', '女'), 
        ('unknow', '未知')], related='send_dog_id.gender', string='申请人性别')
    send_job = fields.Char(related='send_dog_id.job', string='申请人工作')

    # 申请对象
    recieved_dog_id = fields.Many2one('single.dog', ondelete='cascade', string='申请对象')
    received_state = fields.Selection([
        ('waiting', '等待中'),
        ('looking', '寻找中'),
        ('pairing', '配对中'),
        ('pair_succese', '配对成功'),
        ('pair_failed', '配对失败')], related='recieved_dog_id.state', string='申请对象状态')
    recieved_name = fields.Char(related='recieved_dog_id.name', string='对象姓名')
    recieved_age = fields.Integer(related='recieved_dog_id.age', string='对象年龄')
    recieved_gender = fields.Selection([
        ('man', '男'), 
        ('women', '女'), 
        ('unknow', '未知')], related='recieved_dog_id.gender', string='对象性别')
    recieved_job = fields.Char(related='recieved_dog_id.job', string='对象工作')

    # 申请内容
    apply_content = fields.Char(string='申请内容')

    # 申请状态
    state = fields.Selection([
        ('approve', '同意'), 
        ('waiting', '等待中'),
        ('reject', '拒绝')], string='状态', defalut="waiting")
    
    reject_reason = fields.Char(string='拒绝原因')

    pair_history_ids = fields.One2many('pair.history', 'apply_id', string='配对史')  # 一条申请 2条历史

    def action_approve(self):
        """
        同意交往
        """
        if self.send_dog_id.state == 'pairing':
            raise ValidationError('该申请人已经在交往中，你可以拒绝')
        self.write({
            'state': 'approve',
            'pair_history_ids':[
                (0, 0, {
                    'dog_id': self.send_dog_id.id,
                    'pair_dog_id': self.recieved_dog_id.id,
                }), 
                (0, 0, {
                    'dog_id': self.recieved_dog_id.id,
                    'pair_dog_id': self.send_dog_id.id,
                })
                ]
            })
        self.send_dog_id.write({
            'pairing_dog_id': self.recieved_dog_id.id,
            'state': 'pairing'
            })
        self.recieved_dog_id.write({
            'pairing_dog_id': self.send_dog_id.id,
            'state': 'pairing'
            })
    
    def action_reject(self):
        """
        拒绝交往
        """
        action = self.env.ref('cs_single_dog_manage.action_reject_apply_wizard_form').read()[0]
        return action


