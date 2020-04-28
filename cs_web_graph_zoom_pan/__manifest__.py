# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Graph Zoom And Pan',
    'version': '1.0',
    'category': 'CS Web',
    'sequence': 5,
    'summary': 'Graph 视图缩放和平移',
    'description': "",
    'website': 'https://www.loney-cao.github.io',
    'depends': [
        'base',
        'web',
    ],
    'data': [
        'views/web_graph_zoom_pan.xml',
    ],
    'js': ['static/src/js/*.js'],
    'css': ['static/src/css/*.css'],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}
