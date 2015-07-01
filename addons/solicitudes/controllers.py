# -*- coding: utf-8 -*-
from openerp import http

# class Solicitudes(http.Controller):
#     @http.route('/solicitudes/solicitudes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/solicitudes/solicitudes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('solicitudes.listing', {
#             'root': '/solicitudes/solicitudes',
#             'objects': http.request.env['solicitudes.solicitudes'].search([]),
#         })

#     @http.route('/solicitudes/solicitudes/objects/<model("solicitudes.solicitudes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('solicitudes.object', {
#             'object': obj
#         })