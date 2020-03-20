# -*- coding: utf-8 -*-
{
    'name': "RBAC",
    'version': '1.0',
    'category': 'CS Access',
    'sequence': 5,
    'summary': '',
    'description': "",
    'website': 'https://www.loney-cao.github.io',
    'depends': [
        'base',
    ],

    'data': [
        'security/ir.model.access.csv',
        # 'views/search_what_you_want.xml',
        'views/cs_role_view.xml',
    ],
    'qweb': ["static/src/xml/*.xml"],
    'js': ["static/src/js/*.js"],
    'css': ["static/src/css/*.css"],


}

