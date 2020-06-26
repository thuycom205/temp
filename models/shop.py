# -*- coding: utf-8 -*-

from odoo import models, fields, api


class shopify_shop(models.Model):
    _name = 'shopify_app.shop'
    _description = 'Shopify shop information'

    url = fields.Char()
    code = fields.Char()
    id = fields.Integer()
    description = fields.Text()
    install_status = fields.Selection([('active', 'Active'), ('uninstalled', 'Uninstall')
                             ],
                             string="Install status",  default='active')
    billing_status = fields.Selection([('free', 'Free'), ('premium', 'Premium')
                             ],
                             string="Billing status",  default='free')

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class Users(models.Model):

    _inherit = 'res.users'

    org_id = fields.Many2one('shopify_app.shop', 'Organization')



# class Product(models.Model):
#
#     _inherit = 'product.product'
#
#     org_id = fields.Many2one( 'shopify_app.shop', 'Organization')
#
# class SalesOrder(models.Model):
#
#     _inherit = 'sale.order'
#
#     org_id = fields.Many2one( 'shopify_app.shop', 'Organization')

