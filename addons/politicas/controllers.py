# -*- coding: utf-8 -*-
from openerp import http

# class Fomdes(http.Controller):
#     @http.route('/fomdes/fomdes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fomdes/fomdes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fomdes.listing', {
#             'root': '/fomdes/fomdes',
#             'objects': http.request.env['fomdes.fomdes'].search([]),
#         })

#     @http.route('/fomdes/fomdes/objects/<model("fomdes.fomdes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fomdes.object', {
#             'object': obj
#         })