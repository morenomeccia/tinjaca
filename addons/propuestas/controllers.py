# -*- coding: utf-8 -*-
from openerp import http

# class Propuestas(http.Controller):
#     @http.route('/propuestas/propuestas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/propuestas/propuestas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('propuestas.listing', {
#             'root': '/propuestas/propuestas',
#             'objects': http.request.env['propuestas.propuestas'].search([]),
#         })

#     @http.route('/propuestas/propuestas/objects/<model("propuestas.propuestas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('propuestas.object', {
#             'object': obj
#         })