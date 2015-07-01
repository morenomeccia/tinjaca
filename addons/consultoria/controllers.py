# -*- coding: utf-8 -*-
from openerp import http

# class Consultoria(http.Controller):
#     @http.route('/consultoria/consultoria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/consultoria/consultoria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('consultoria.listing', {
#             'root': '/consultoria/consultoria',
#             'objects': http.request.env['consultoria.consultoria'].search([]),
#         })

#     @http.route('/consultoria/consultoria/objects/<model("consultoria.consultoria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('consultoria.object', {
#             'object': obj
#         })