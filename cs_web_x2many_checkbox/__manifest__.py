# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web X2Many CheckBox',
    'version': '1.0',
    'category': 'CS Web',
    'sequence': 5,
    'summary': 'Form表单视图中，对于X2Many字段的Tree视图，展示CheckBox复选框',
    'description': "",
    'website': 'https://www.loney-cao.github.io',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/web_x2many_checkbox.xml',
    ],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
