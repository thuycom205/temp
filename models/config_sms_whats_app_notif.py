from odoo import models, fields


class ConfigSmsWhatsAppNotification(models.Model):
    _name = 'config.sms.whats.app.notification'

    account_sid = fields.Char(string='Twilio Account Sid')
    authentication_token = fields.Char(string='Authentication Token')
    whatsapp_sender_id = fields.Char(string='WhatsApp Sender ID')
    sms_sender_id = fields.Char(string='SMS Sender ID')
    admin_mobile_number = fields.Char(string='Admin Mobile Number')

    default_type = fields.Selection([
        ('sms', 'SMS'),
        ('whatsapp', 'WhatsApp')])
