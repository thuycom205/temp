from odoo import fields, models


class MessageOrderConfirm(models.Model):
    _name = 'message.order.confirm'

    message_name = fields.Char(string='Name')
    message_body = fields.Text(string='Message')
    create_discount = fields.Boolean()
    discount_amount = fields.Integer(string='Discount Amount')