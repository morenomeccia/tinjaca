# -*- coding: utf-8 -*-
from openerp import http

# class Administracion(http.Controller):
#     @http.route('/administracion/administracion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/administracion/administracion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('administracion.listing', {
#             'root': '/administracion/administracion',
#             'objects': http.request.env['administracion.administracion'].search([]),
#         })

#     @http.route('/administracion/administracion/objects/<model("administracion.administracion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('administracion.object', {
#             'object': obj
#         })