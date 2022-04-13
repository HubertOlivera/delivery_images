# -*- coding: utf-8 -*-
# from odoo import http


# class DeliveryImages(http.Controller):
#     @http.route('/delivery_images/delivery_images/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/delivery_images/delivery_images/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('delivery_images.listing', {
#             'root': '/delivery_images/delivery_images',
#             'objects': http.request.env['delivery_images.delivery_images'].search([]),
#         })

#     @http.route('/delivery_images/delivery_images/objects/<model("delivery_images.delivery_images"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('delivery_images.object', {
#             'object': obj
#         })
