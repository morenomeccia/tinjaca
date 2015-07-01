# -*- coding: utf-8 -*-
from openerp import http

# class Archivo(http.Controller):
#     @http.route('/archivo/archivo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/archivo/archivo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('archivo.listing', {
#             'root': '/archivo/archivo',
#             'objects': http.request.env['archivo.archivo'].search([]),
#         })

#     @http.route('/archivo/archivo/objects/<model("archivo.archivo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('archivo.object', {
#             'object': obj
#         })