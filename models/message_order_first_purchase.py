from odoo import fields, models


class MessageOrderCrmFirstPurchase(models.Model):
    _name = 'message.order.crm.first.purchase'

    message_name = fields.Char(string='Name')
    message_body = fields.Text(string='Message')
    create_discount = fields.Boolean()
    discount_amount = fields.Integer(string='Discount Amount')