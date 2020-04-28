# -*- coding: utf-8 -*-
{
    'name': "Export Xml",

    'summary': """将记录导出为xml文件""",

    'description': """""",

    'author': "Loney",
    'website': "https://loneycao.gitee.io/",

    'category': 'tools',
    'version': '0.1',

    'depends': ['web'],

    'data': [
        'wizard/export_xml_wizard_views.xml',
    ],
    'qweb': ["static/src/xml/*.xml"],
    'js': ["static/src/js/*.js"],
    'css': ["static/src/css/*.css"],
    'post_load': 'patch_fvg',


}

