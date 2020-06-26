from odoo import models, fields


class ConfigManualOrderCrm(models.Model):
    _name = 'config.manual.order.crm'

    manual_order_crm_line = fields.One2many('config.manual.order.crm.line','manual_order_crm_id')
    send_whatsapp = fields.Selection([('send_web', 'WhatsApp Web'),
                                      ('send_desktop', 'WhatsApp Desktop')])

    def message_template(self):
        view_id = self.env.ref('whatsapp.message_template_form').id
        result = {
            "type": "ir.actions.act_window",
            "res_model": "message.template",
            'view_mode': 'form',
            'target': 'new',
            "views_id": view_id,
            "name": "Message Template",
        }
        return result


class ConfigManualOrderCrmLine(models.Model):
    _name = 'config.manual.order.crm.line'
    manual_order_crm_id = fields.Many2one('config.manual.order.crm')
    checkout_user = fields.Char(string='Checkout,User')
    date = fields.Date(string='Date')
    amount = fields.Char(string='Amount')
    status = fields.Char(string='status')
