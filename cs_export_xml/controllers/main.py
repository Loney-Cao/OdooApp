from odoo import http
from odoo.http import request, content_disposition
import os


class ExportXmlController(http.Controller):

    @http.route('/cs_export_xml/download_xml_file/<string:file_name>', auth='user', type='http')
    def download_xml_file(self, file_name, **kwargs):

        file_path = os.path.join(os.path.dirname(__file__), '../static/export/export.xml')
        file = open(file_path, 'rb').read()

        return request.make_response(file, [
            ('Content-Type', 'application/octet-stream'),
            ('Content-Length', len(file)),
            ('Content-Disposition', content_disposition('%s.xml' % file_name))
        ])

