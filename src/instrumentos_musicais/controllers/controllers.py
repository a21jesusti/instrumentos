# -*- coding: utf-8 -*-
# from odoo import http


# class InstrumentosMusicais(http.Controller):
#     @http.route('/instrumentos_musicais/instrumentos_musicais/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instrumentos_musicais/instrumentos_musicais/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('instrumentos_musicais.listing', {
#             'root': '/instrumentos_musicais/instrumentos_musicais',
#             'objects': http.request.env['instrumentos_musicais.instrumentos_musicais'].search([]),
#         })

#     @http.route('/instrumentos_musicais/instrumentos_musicais/objects/<model("instrumentos_musicais.instrumentos_musicais"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instrumentos_musicais.object', {
#             'object': obj
#         })
