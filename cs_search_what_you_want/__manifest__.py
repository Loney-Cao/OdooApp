# -*- coding: utf-8 -*-
{
    'name': "搜你所想",

    'summary': """""",

    'description': """""",

    'author': "Loney",
    'website': "http://www.baidu.net",

    'category': 'search',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/search_what_you_want.xml',
        'views/search_view.xml',
    ],
    'qweb': ["static/src/xml/*.xml"],
    'js': ["static/src/js/*.js"],
    'css': ["static/src/css/*.css"],


}

