from odoo import fields, models, _
from odoo.exceptions import UserError


class ConfigPhoneNumber(models.Model):
    _name = 'config.phone.number'

    config_basic_id = fields.Many2one('config.basic.whats.app')
    country_code = fields.Char(string='Country Code')
    phone_number = fields.Char(string='Phone Number')
    agent_name = fields.Many2one('res.users', string='Agent Name')
    agent_role = fields.Char(string='Agent Role')
    agent_avatar = fields.Binary()
    url_image = fields.Char('URL for avatar')

    def _default_note(self):
        note = 'Example - 8:30AM is 0830 and 8:30PM is 2030. By default, hours are set from 0000 to 2359 which means ' \
               'chat agent is active all the time. To disable the chat agent for an entire day, set 0000 to 0000 '

        return note

    default_note = fields.Text(string='Note', default=_default_note)

    def confirm(self):
        for rec in self:
            if not rec.phone_number.isnumeric():
                raise UserError(_('Số điện thoại không hợp lệ.'))
        return {
            'type': 'ir.actions.client',
            'tag': 'button_template_client_action',
        }
