from odoo import models, fields


class ConfigShopifyCart(models.Model):
    _name = 'config.shopify.cart'

    lang_id = fields.Many2one('res.lang', string='Ngôn ngữ')
    phone = fields.Char(string='Số điện thoại')
    country_code = fields.Char(string='mã vùng')

    use_coupon_discount = fields.Boolean(default=False)
    coupon_discount = fields.Integer(string='Giảm giá')

    use_coupon_code = fields.Boolean(default=False)
    coupon_code = fields.Char(string='Mã giảm giá')
    include_discount_coupon = fields.Boolean(string='Áp dụng giảm giá')

    # defaut information for message
    def _default_infomation_message(self):
        mess = 'Hi {{customer_name}}, thank you for your purchase of {{order_value}} from {{shop_name}}. Your order ' \
               'is getting ready and we will notify you when it has been shipped. You can view your order here {{' \
               'order_ID}} {{order_status_url}}'
        return mess
    information_message = fields.Text(string='Thông tin message',
                                      default=_default_infomation_message)
    # store
    lang_store_id = fields.Many2one('res.lang', string='Ngôn ngữ cho cửa hàng')
    add_to_cart = fields.Boolean(default=False)
    buy_product = fields.Boolean(default=False)
    landing_product = fields.Boolean(default=False)
    checkout_product = fields.Boolean(default=False)

    # message logs
    # message_log = fields.One2many('message.logs', 'message_id')


