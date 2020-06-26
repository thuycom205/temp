from odoo import models, fields


class ConfigShopifyCashOnDelivery(models.Model):
    _name = 'config.shopify.cash.on.delivery'

    lang_id = fields.Many2one('res.lang', string='Ngôn ngữ')
    phone = fields.Char(string='Số điện thoại')

    # defaut information for message
    def _default_information_message(self):
        mess = 'Hi {{customer_name}}, thank you for your purchase of {{order_value}} from {{shop_name}}. Your order ' \
               'is getting ready and we will notify you when it has been shipped. You can view your order here {{' \
               'order_ID}} {{order_status_url}}'
        return mess

    information_message = fields.Text(string='Thông tin message',
                                      default=_default_information_message)
    order_confirmed_tag = fields.Char(string='Đặt hàng xác nhận thẻ')
    order_cancelled_tag = fields.Char(string='Đơn hàng đã huỷ thẻ')
    no_response_tag = fields.Char(string='Không có thẻ phản hồi')

    check_order_cancel = fields.Boolean()
    check_no_response = fields.Boolean()

    check_call = fields.Boolean()
    country_code = fields.Char(string='Mã quốc gia')
    phone_number = fields.Char(string='Số điện thoai')

    check_mail = fields.Boolean()
    email = fields.Char(string='email')

    lang_store_id = fields.Many2one('res.lang', string='Ngôn ngữ cho cửa hàng')
    add_to_cart = fields.Boolean(default=False)
    buy_product = fields.Boolean(default=False)
    landing_product = fields.Boolean(default=False)
    checkout_product = fields.Boolean(default=False)

