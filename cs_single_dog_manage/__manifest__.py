# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Single Dog Manage',
    'version': '1.0',
    'category': 'CS System',
    'sequence': 5,
    'summary': '单身狗系统',
    'description': "",
    'website': 'https://www.loney-cao.github.io',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/single_dog_views.xml',
        'views/single_dog_tag_views.xml',
        'views/single_dog_manage_menus.xml',
        'wizard/looking_dog_wizard_views.xml',
        'wizard/reject_apply_wizard_views.xml',
        'views/assets.xml',
    ],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
