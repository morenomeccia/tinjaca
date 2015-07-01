# -*- coding: utf-8 -*-
from openerp import http

# class Presidencia(http.Controller):
#     @http.route('/presidencia/presidencia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/presidencia/presidencia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('presidencia.listing', {
#             'root': '/presidencia/presidencia',
#             'objects': http.request.env['presidencia.presidencia'].search([]),
#         })

#     @http.route('/presidencia/presidencia/objects/<model("presidencia.presidencia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('presidencia.object', {
#             'object': obj
#         })