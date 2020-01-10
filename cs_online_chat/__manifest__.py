# -*- coding: utf-8 -*-
{
    'name': "聊天室",

    'summary': """""",

    'description': """""",

    'author': "Loney",
    'website': "http://www.baidu.net",

    'category': 'search',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/cs_online_chat.xml',
        'views/chatting_view.xml',
    ],
    'qweb': ["static/src/xml/*.xml"],
    'js': ["static/src/js/*.js"],
    'css': ["static/src/css/*.css"],


}

