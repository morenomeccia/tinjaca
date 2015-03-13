# -*- coding: utf-8 -*-
from openerp import http

# class Recuperaciones(http.Controller):
#     @http.route('/recuperaciones/recuperaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recuperaciones/recuperaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('recuperaciones.listing', {
#             'root': '/recuperaciones/recuperaciones',
#             'objects': http.request.env['recuperaciones.recuperaciones'].search([]),
#         })

#     @http.route('/recuperaciones/recuperaciones/objects/<model("recuperaciones.recuperaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recuperaciones.object', {
#             'object': obj
#         })