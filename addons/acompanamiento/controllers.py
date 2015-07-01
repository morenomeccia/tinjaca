# -*- coding: utf-8 -*-
from openerp import http

# class Acompanamiento(http.Controller):
#     @http.route('/acompanamiento/acompanamiento/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/acompanamiento/acompanamiento/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('acompanamiento.listing', {
#             'root': '/acompanamiento/acompanamiento',
#             'objects': http.request.env['acompanamiento.acompanamiento'].search([]),
#         })

#     @http.route('/acompanamiento/acompanamiento/objects/<model("acompanamiento.acompanamiento"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('acompanamiento.object', {
#             'object': obj
#         })