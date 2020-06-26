# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    shopify_name = fields.Char(
        "Shopify product name", help="Shopify product name")
    shopify_product_id = fields.Float(
        "Shopify product id",default = 0.0, help="Shopify product id")




class ProductProduct(models.Model):
    _inherit = 'product.product'

    shopify_variant_name = fields.Char(
        "Shopify variant  product name", help="Shopify variant product name")

    shopify_variant_product_id = fields.Float(
        "Shopify variant product id", default = 0.0, help="Shopify variant product id")
