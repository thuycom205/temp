from odoo import models, fields, api


class ConfigButtonTextDesign(models.Model):
    _name = 'config.button.text.design'

    user_id = fields.Many2one('res.users')
    color_button_text = fields.Selection([('single', 'Single colour'), ('grandient', 'Grandient of two colours')])
    background_colour_1 = fields.Char(string='Background colour 2')
    background_colour_2 = fields.Char(string='Background colour 2')
    icon_colour = fields.Char(string='Icon colour')
    button_color = fields.Char(string='Button text colour')
    chat_button_text = fields.Char(string='Chat Button Text')
    whatsapp_message_body = fields.Text(string='WhatsApp Message Body')
    include_url = fields.Boolean()


    @api.model
    def create(self, vals):
        res = super(ConfigButtonTextDesign, self).create(vals)
        current_id = self.env['res.users'].search([('id', '=', self.env.uid)])
        val = {
            'config_button_color': res.id
        }
        res.user_id = current_id.id
        current_id.update(val)
        return res

    def confirm(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'button_template_client_action',
        }






