from odoo import models, fields, api


class ConfigCalloutCard(models.Model):
    _name = 'config.callout.card'
    user_id = fields.Many2one('res.users')
    show_callout_button = fields.Boolean()
    callout_car_text = fields.Char(string='')
    callout_card_delay = fields.Char(string='Callout card delay')

    @api.model
    def create(self, vals):
        res = super(ConfigCalloutCard, self).create(vals)
        current_id = self.env['res.users'].search([('id', '=', self.env.uid)])
        val = {
            'config_callout_card_id': res.id
        }
        res.user_id = current_id.id
        current_id.update(val)
        return res

    def confirm(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'button_template_client_action',
        }
