# -*- coding: utf-8 -*-
from openerp import http

# class Atencion(http.Controller):
#     @http.route('/atencion/atencion/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/atencion/atencion/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('atencion.listing', {
#             'root': '/atencion/atencion',
#             'objects': http.request.env['atencion.atencion'].search([]),
#         })

#     @http.route('/atencion/atencion/objects/<model("atencion.atencion"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('atencion.object', {
#             'object': obj
#         })