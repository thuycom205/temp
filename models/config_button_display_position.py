from odoo import models, fields, api


class ConfigButtonDisplayPosition(models.Model):
    _name = 'config.button.display.position'
    user_id = fields.Many2one('res.users')
    chat_button_display = fields.Selection([('mobile_desktop', 'Mobile + Desktop'),
                                            ('mobile_only', 'Mobile only'),
                                            ('desktop_only', 'Desktop only')])

    button_mobile_position = fields.Selection([('mobile_left', 'Left'),
                                               ('mobile_right', 'Right')])

    button_desktop_position = fields.Selection([('desktop_left', 'Left'),
                                                ('desktop_right', 'Right')])

    height_mobile = fields.Integer(string='Height Mobile')
    height_desktop = fields.Integer(string='Height Desktop')

    edge_mobile = fields.Integer(string='EDGE mobile')
    edge_desktop = fields.Integer(string='EDGE desktop')

    set_height_button_page = fields.Boolean()
    height_mobile_page = fields.Integer(string='Height Mobile Page')
    height_desktop_page = fields.Integer(string='Height Desktop Height')


    @api.model
    def create(self, vals):
        res = super(ConfigButtonDisplayPosition, self).create(vals)
        current_id = self.env['res.users'].search([('id', '=', self.env.uid)])
        val = {
            'config_button_display_position_id': res.id
        }
        res.user_id = current_id.id
        current_id.update(val)
        return res

    def confirm(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'button_template_client_action',
        }
