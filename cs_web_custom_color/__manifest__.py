# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Custom Color',
    'version': '1.0',
    'category': 'CS Web',
    'sequence': 5,
    'summary': '自定义视图 背景颜色',
    'description': "",
    'website': 'https://www.loney-cao.github.io',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/web_custom_color.xml',
    ],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
