# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo.tests import tagged
from odoo.tests.common import HttpCase, TransactionCase


@tagged('post_install', '-at_install')
class TestUi(HttpCase):
    def test_ui(self):
        print('*'*100)
        print('测试开始')
        self.start_tour("/web", 'single_dog_tour_test', login='admin')
        dog = self.env['single.dog'].search([('name', '=', '小明')])
        self.assertEqual(len(dog.ids), 1, "单身狗只有小明一个")
        print('单身狗是--> ', dog.name)
        print('测试结束')
