# -*- coding: utf-8 -*-
from openerp import http

# class Aprobacion(http.Controller):
#     @http.route('/aprobacion/aprobacion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aprobacion/aprobacion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aprobacion.listing', {
#             'root': '/aprobacion/aprobacion',
#             'objects': http.request.env['aprobacion.aprobacion'].search([]),
#         })

#     @http.route('/aprobacion/aprobacion/objects/<model("aprobacion.aprobacion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aprobacion.object', {
#             'object': obj
#         })