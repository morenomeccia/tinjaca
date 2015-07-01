# -*- coding: utf-8 -*-
from openerp import http

# class Estadistica(http.Controller):
#     @http.route('/estadistica/estadistica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estadistica/estadistica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estadistica.listing', {
#             'root': '/estadistica/estadistica',
#             'objects': http.request.env['estadistica.estadistica'].search([]),
#         })

#     @http.route('/estadistica/estadistica/objects/<model("estadistica.estadistica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estadistica.object', {
#             'object': obj
#         })