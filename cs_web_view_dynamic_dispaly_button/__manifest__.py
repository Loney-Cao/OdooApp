# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Dynamic Dispaly Button',
    'version': '1.0',
    'category': 'CS Web',
    'sequence': 5,
    'summary': '视图动态显示创建、编辑等按钮',
    'description': "",
    'website': 'https://www.loney-cao.github.io',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/web_view_dynamic_dispaly_button.xml',
    ],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
