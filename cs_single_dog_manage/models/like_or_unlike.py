'''
@Author: LoneyCao
@Date: 2020-04-12 15:16:02
@LastEditTime: 2020-04-14 22:07:24
@LastEditors: Please set LastEditors
@Description: 踩赞
@FilePath: /cscloud/OdooApp/cs_single_dog_manage/models/like_or_unlike.py
'''
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LikeOrUnlike(models.Model):
    _name = 'like.or.unlike'
    _description = 'Like Or Unlike'  # 赞 踩

    comment_id = fields.Many2one('single.dog.comment', ondelete='cascade', string='评论')
    tag_id = fields.Many2one('single.dog.tag', ondelete='cascade', string='标签')

    like = fields.Boolean(string="赞")
    unlike = fields.Boolean(string='踩')
    dog_id = fields.Many2one('single.dog', string='踩赞人')
    







