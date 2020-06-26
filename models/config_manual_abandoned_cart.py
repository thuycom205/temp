from odoo import models, fields


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
    date = fields.Date(string='Date')
    amount = fields.Char(string='Amount')
    status = fields.Char(string='status')
    # tags = fields.Many2many('message.manual.abandoned.1')
