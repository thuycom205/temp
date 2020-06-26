# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ShopifyOrder(models.Model):
    _inherit = 'sale.order'

    shopify_name = fields.Char(
        "Shopify order name", help="Shopify order name")

    shopify_id = fields.Float(
        "Shopify order id", help="Shopify order id")


class ShopifyOrderLine(models.Model):
    _inherit = 'sale.order.line'

    shopify_name = fields.Char(
        "Shopify name", help="Shopify name")

    shopify_id = fields.Float(
        "Shopify  id", help="Shopify id")
