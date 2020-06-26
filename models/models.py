# -*- coding: utf-8 -*-

from odoo import models, fields, api
import shopify


class shopify_app(models.Model):
    _name = 'shopify_app.shopify_app'
    _description = 'shopify_app.shopify_app'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

    def createVariant(self,**kwargs):
        new_product = shopify.Product()

        new_product.options = [{"name": "Colour", "values": ["Red", "Blue"]}, {"name": "Size", "values": ["M", "L"]}]

        red_variant = shopify.Variant({"title": "v1", "option1": "Red", "option2": "M"})
        blue_variant = shopify.Variant({"title": "v2", "option1": "Blue", "option2": "L"})

        new_product.variants = [red_variant, blue_variant]

        new_product.save()

    def findProductBaseOnTags(self,id):
        tag = 'mn_rental'
        x = id
        y = 'test'
       # product = shopify.Product.find( [dict(tags='st_rental',limit="100")]);
        #product = shopify.Product.find(None,'product',tags=("tags", "like", "st_rental"));
       # product = shopify.Product.find(None,'product',product = {'tags': 'st_rental'});


        x = 2




