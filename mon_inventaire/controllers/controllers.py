# -*- coding: utf-8 -*-
# from odoo import http


# class MonInventaire(http.Controller):
#     @http.route('/mon_inventaire/mon_inventaire/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mon_inventaire/mon_inventaire/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mon_inventaire.listing', {
#             'root': '/mon_inventaire/mon_inventaire',
#             'objects': http.request.env['mon_inventaire.mon_inventaire'].search([]),
#         })

#     @http.route('/mon_inventaire/mon_inventaire/objects/<model("mon_inventaire.mon_inventaire"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mon_inventaire.object', {
#             'object': obj
#         })
