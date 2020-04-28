'''
@Author: LoneyCao
@Date: 2020-04-11 11:35:52
@LastEditTime: 2020-04-14 23:13:27
@LastEditors: Please set LastEditors
@Description: 单身狗信息
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/models/single_dog.py
'''
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SingleDog(models.Model):
    _name = 'single.dog'
    _description = 'Single Dog'  # 单身狗

    # 个人信息资料
    user_id = fields.Many2one('res.users', string='用户')
    name = fields.Char(string='姓名')
    age = fields.Integer(string='年龄')
    gender = fields.Selection([
        ('man', '男'), 
        ('women', '女'), 
        ('unknow', '未知')], string='性别')
    job = fields.Char(string='工作')

    # 期望对象条件

    # 收到的配对申请
    received_pair_apply_ids = fields.One2many('pair.apply', 'recieved_dog_id', string='收到的配对申请')  # 别人的申请对象是我

    # 发出的配对申请
    send_pair_apply_ids = fields.One2many('pair.apply', 'send_dog_id', string='发出的配对申请')  # 我的申请

    # 正在交往的对象
    pairing_dog_id = fields.Many2one('single.dog', ondelete='cascade', string='正在交往对象')
    pairing_state = fields.Selection([
        ('waiting', '等待中'),
        ('looking', '寻找中'),
        ('pairing', '配对中'),
        ('pair_succese', '配对成功'),
        ('pair_failed', '配对失败')], related='pairing_dog_id.state', string='对象状态')
    pairing_name = fields.Char(related='pairing_dog_id.name', string='对象姓名')
    pairing_age = fields.Integer(related='pairing_dog_id.age', string='对象年龄')
    pairing_gender = fields.Selection([
        ('man', '男'), 
        ('women', '女'), 
        ('unknow', '未知')], related='pairing_dog_id.gender', string='对象性别')
    pairing_job = fields.Char(related='pairing_dog_id.job', string='对象工作')

    # 配对历史
    pair_history_ids = fields.One2many('pair.history', 'dog_id', string='配对史')

    # 评价
    comment_ids = fields.One2many('single.dog.comment', 'dog_id', string='评价')  # 我评价他人

    # 标签
    tag_ids = fields.One2many('single.dog.tag', 'dog_id', string='标签')
    page_tag_ids = fields.One2many('single.dog.tag', compute='_compute_page_tag_ids',  string='我的标签')


    # 当前状态

    state = fields.Selection([
        ('waiting', '等待中'),
        ('looking', '寻找中'),
        ('pairing', '配对中'),
        ('pair_succese', '配对成功'),
        ('pair_failed', '配对失败')], default='waiting', string='状态')
    
    # @api.depends('tag_ids')
    def _compute_page_tag_ids(self):
        for record in self:
            record.page_tag_ids = record.tag_ids.filtered(lambda tag: tag.is_show)

    
    def action_looking_for(self):
        """
        查找心仪对象
        """
        if self.state == 'waiting':
            self.write({'state': 'looking'})
            
        action = self.env.ref('cs_single_dog_manage.action_looking_dog_wizard_form').read()[0]
        return action
    
    def preview_my_tag(self):
        """
        查看我的标签
        """
        action = self.env.ref('cs_single_dog_manage.action_single_dog_tag').read()[0]
        action.update({
            'domain': [('dog_id', '=', self.id)],
            'context': {
                'default_dog_id': self.id,
                'default_pari_dog_id': self.id,
            }
        })
        return action







