# -*- coding: utf-8 -*-

from odoo import models, fields, api

class beckhoff_view_extensions(models.Model):
    _inherit = 'product.product'

    list_price = fields.Float(track_visibility='OnChange')
    name = fields.Char(track_visibility='OnChange')

class ProductTemplateChangeTrack(models.Model):
    _inherit = 'product.template'

    list_price = fields.Float(track_visibility='OnChange')
    name = fields.Char(track_visibility='OnChange')

class PartnerChangeData(models.Model):
    _inherit = 'res.partner'

    name = fields.Char(track_visibility='OnChange')
    email = fields.Char(track_visibility='OnChange')
    city = fields.Char(track_visibility='OnChange')
    street = fields.Char(track_visibility='OnChange')


#    Include OnChange Events for product: price, category, name etc.
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
