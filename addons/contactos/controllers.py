# -*- coding: utf-8 -*-
from openerp import http

# class ../tinjaca/addons/personas(http.Controller):
#     @http.route('/../tinjaca/addons/personas/../tinjaca/addons/personas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../tinjaca/addons/personas/../tinjaca/addons/personas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../tinjaca/addons/personas.listing', {
#             'root': '/../tinjaca/addons/personas/../tinjaca/addons/personas',
#             'objects': http.request.env['../tinjaca/addons/personas.../tinjaca/addons/personas'].search([]),
#         })

#     @http.route('/../tinjaca/addons/personas/../tinjaca/addons/personas/objects/<model("../tinjaca/addons/personas.../tinjaca/addons/personas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../tinjaca/addons/personas.object', {
#             'object': obj
#         })