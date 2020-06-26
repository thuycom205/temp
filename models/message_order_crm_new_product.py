from odoo import fields, models


class MessageOrderCrmNewProduct(models.Model):
    _name = 'message.order.crm.new.product'

    message_name = fields.Char(string='Name')
    message_body = fields.Text(string='Message')
    create_discount = fields.Boolean()
    discount_amount = fields.Integer(string='Discount Amount')