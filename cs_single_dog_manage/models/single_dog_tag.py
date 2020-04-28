'''
@Author: your name
@Date: 2020-04-12 14:57:15
@LastEditTime: 2020-04-14 22:32:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/models/single_dog_tag.py
'''
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SingleDogTag(models.Model):
    _name = 'single.dog.tag'
    _description = 'Single Dog Tag'  # 单身狗标签


    dog_id = fields.Many2one('single.dog', ondelete='cascade', string='单身狗')
    # 交往对象
    pari_dog_id = fields.Many2one('single.dog', ondelete='cascade', string='对象')

    name = fields.Char(string='标签')
    is_show = fields.Boolean(string="个人信息页展示", default=False)
    
    like = fields.Boolean(string="赞")
    like_num = fields.Integer(string='赞')
    unlike = fields.Boolean(string='踩')
    unlike_num = fields.Integer(string='踩')

    like_or_unlik_ids = fields.One2many('like.or.unlike', 'tag_id', string='赞踩记录')





