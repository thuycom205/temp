from odoo import models, fields
import shopify
import json
from datetime import datetime

class ConfigManualAbandonedCart(models.Model):
    _name = 'config.manual.abandoned.cart'

    manual_abandoned_cart_line = fields.One2many('config.manual.abandoned.cart.line', 'manual_abandoned_cart_id')
    send_whatsapp = fields.Selection([('send_web', 'WhatsApp Web'),
                                      ('send_desktop', 'WhatsApp Desktop')])

    # function view form message 1
    def edit_message_1(self):
        view_id = self.env.ref('whatsapp.message_manual_abandoned_1_form').id
        result = {
            "type": "ir.actions.act_window",
            "res_model": "message.manual.abandoned.1",
            'view_mode': 'form',
            'target': 'new',
            "views_id": view_id,
            "name": "Message 1",
        }
        return result

    # function view form message 2
    def edit_message_2(self):
        view_id = self.env.ref('whatsapp.message_manual_abandoned_2_form').id
        result = {
            "type": "ir.actions.act_window",
            "res_model": "message.manual.abandoned.2",
            'view_mode': 'form',
            'target': 'new',
            "views_id": view_id,
            "name": "Message 1",
        }
        return result



class ConfigManualAbandonedCartLine(models.Model):
    _name = 'config.manual.abandoned.cart.line'
    manual_abandoned_cart_id = fields.Many2one('config.manual.abandoned.cart')
    checkout_user = fields.Char(string='Checkout,User')
    checkout_id = fields.Char(string='Checkout')
    customer_name = fields.Char(string='User')
    date = fields.Date(string='Date')
    amount = fields.Char(string='Amount')
    status = fields.Char(string='status')



    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        x=1
        return super(ConfigManualAbandonedCartLine, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit,
                                                              order=order)


class ShopifyCheckoutUsedForAbandonnedCart(models.Model):
    _name = 'whatsapp.shopify.checkout'
    checkout_id = fields.Char(string='Checkout')
    checkout_iden = fields.Float(string= 'Checkout id',digits=(0, 0))
    customer_name = fields.Char(string='Customer Name')
    customer_phone = fields.Char(string='Phone')
    customer_email = fields.Char(string='Customer Email')
    date = fields.Date(string='Date')
    amount = fields.Char(string='Amount')
    status = fields.Char(string='status')

    recover_status = fields.Selection([('recovered', 'Recovered'), ('not_recovered', 'Not Recovered')
                                       ],
                                      string="Recovered status", default='not_recovered')

    send_mess1_status = fields.Selection([('sent', 'Send Message 1'), ('not_sent', 'Send Message 1')
                                          ],
                                         string="Sent message 1", default='not_sent')

    send_mess2_status = fields.Selection([('sent', 'Send Message1'), ('not_sent', 'Send Message 2')
                                          ],
                                         string="Sent message 2", default='not_sent')

    def update_abandoned_cart(self, **kwargs):
        domain = kwargs['domain']
        shop = self.env['shopify_app.shop'].sudo().search([('url', '=',domain)])
        token = shop.code
        session = shopify.Session(domain, '2019-04', token)
        shopify.ShopifyResource.activate_session(session)

        #find the abandoned cart with the maxium id existing in odoo
        self._cr.execute("""SELECT
        "whatsapp_shopify_checkout".id
        FROM
        "whatsapp_shopify_checkout"
        WHERE("whatsapp_shopify_checkout"."id" > '0') ORDER
        BY
        "whatsapp_shopify_checkout"."checkout_iden"
        DESC
        limit
        1
        """)
        checkout = self._cr.fetchall()

        # checkout = self.env['whatsapp.shopify.checkout'].sudo().search([('id', '>', 0)],order="checkout_iden desc", limit=1)

        if not checkout:
            abandonedCarts = shopify.Checkout.find()
            if abandonedCarts:
                vals = []
                for abandonedCart in abandonedCarts:
                    cid = float(abandonedCart.attributes['id'])
                    email = abandonedCart.attributes['email']
                    phone = abandonedCart.attributes['phone']
                    total_price  = abandonedCart.attributes['total_price']
                    vals.append({
                                 'checkout_iden': cid,
                                  'checkout_id' : repr(cid),
                                  'customer_email' : email,
                                  'customer_phone' :phone,
                                  'amount' : total_price
                                 }
                                )

                self.env['whatsapp.shopify.checkout'].sudo().create(vals)
        else:
            for pid in checkout:
                abandonedCart = self.browse(pid)
                aid = abandonedCart['checkout_iden']
                aidInt = int(aid)
                updatedCheckouts = shopify.Checkout.find( since_id=aidInt)
                if updatedCheckouts:
                    x='need to update'

    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        self.update_abandoned_cart(domain='meogaming.myshopify.com')
        # self.cron_fetch_abandoned_cart()
        return super(ShopifyCheckoutUsedForAbandonnedCart, self).search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)

    def cron_fetch_abandoned_cart(self):
        todayStr = datetime.today().strftime('%Y-%m-%d')
        checkout = self.env['whatsapp.shopify.checkout'].sudo().search([('id', '>', 0)],order="checkout_iden desc", limit=1)

        shops = self.env['shopify_app.shop'].sudo().search([('id' , '>' , 0)])
        for shop in shops:
            # get the offline access code
            token = shop['code']
            domain = shop['url']

            session = shopify.Session(domain,'2019-04', token)
            shopify.ShopifyResource.activate_session(session)

            checkouts = shopify.Checkout.find(updated_at_min=todayStr)

            updatedCheckouts = shopify.Checkout.find( since_id=12950897623172)
            checkoutCount = shopify.Checkout.get('count')

            client = shopify.GraphQL()
            query = '''
               {
                  products(first:10, query:"tag:rental") {
                    edges {
                      node {
                        id
                        title
                      }
                    }
                  }
                }
              '''
            result = client.execute(query)
            d = json.loads(result)
            if checkouts:
                for checkout in checkouts:
                    #update or create
                    cart_token = checkout.attributes['cart_token']
                    exist_checkout = self.sudo().search([('cart_token', 'like', cart_token)])
                    if not exist_checkout:
                        #todo:
                        vals = {}
                        # self.create({
                        #     vals
                        # })








