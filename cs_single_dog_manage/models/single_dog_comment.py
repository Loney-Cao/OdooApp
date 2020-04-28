'''
@Author: LoneyCao
@Date: 2020-04-12 14:45:21
@LastEditTime: 2020-04-14 22:30:52
@LastEditors: Please set LastEditors
@Description: 单身狗评价
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/models/single_dog_comment.py
'''
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SingleDogComment(models.Model):
    _name = 'single.dog.comment'
    _description = 'Single Dog Comment'  # 单身狗评价


    dog_id = fields.Many2one('single.dog', ondelete='cascade', string='单身狗')
    # 交往对象
    pari_dog_id = fields.Many2one('single.dog', ondelete='cascade', string='对象')

    comment = fields.Text(string='评论')

    like = fields.Boolean(string="赞")
    like_num = fields.Integer(string='赞数')
    unlike = fields.Boolean(string='踩')
    unlike_num = fields.Integer(string='踩数')

    like_or_unlik_ids = fields.One2many('like.or.unlike', 'comment_id', string='赞踩记录')
    







