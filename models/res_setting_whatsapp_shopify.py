from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    account_sid = fields.Char(string='Twilio Account Sid')

    authentication_token = fields.Char(string='Authentication Token')
    whatsapp_sender_id = fields.Char(string='WhatsApp Sender ID')
    sms_sender_id = fields.Char(string='SMS Sender ID')
    admin_mobile_number = fields.Char(string='Admin Mobile Number')
    notification_type = fields.Selection([('sms','SMS'),('app','WhatsApp')])
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            account_sid=self.env['ir.config_parameter'].sudo().get_param('whatsapp.account_sid')
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('whatsapp.account_sid', self.account_sid)
