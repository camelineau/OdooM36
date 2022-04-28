# -*- coding: utf-8 -*-
# from odoo import http


# class GestionAlternant(http.Controller):
#     @http.route('/gestion_alternant/gestion_alternant/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_alternant/gestion_alternant/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_alternant.listing', {
#             'root': '/gestion_alternant/gestion_alternant',
#             'objects': http.request.env['gestion_alternant.gestion_alternant'].search([]),
#         })

#     @http.route('/gestion_alternant/gestion_alternant/objects/<model("gestion_alternant.gestion_alternant"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_alternant.object', {
#             'object': obj
#         })
