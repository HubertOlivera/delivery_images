# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class delivery_images(models.Model):
#     _name = 'delivery_images.delivery_images'
#     _description = 'delivery_images.delivery_images'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
