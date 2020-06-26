from odoo import fields, models


class MessageManualAbandoned1(models.Model):
    _name = 'message.manual.abandoned.1'
    message_name = fields.Char(string='Name')

    def _default_message_manual_1(self):
        mess = '{{shop_name}}: Hi {{first_name}}, we noticed there were a few items left in your shopping cart 🛒{{cart_items}}If you’re ready to complete your order, your cart awaits you at 👉 {{checkout_url}}'
        return mess

    message_body = fields.Text(string='Message', default=_default_message_manual_1)
    create_discount = fields.Boolean(string='Create discount code')
    discount_amount = fields.Integer(string='Discount amount(in %)')
