from odoo import models, fields, api


class ConfigPageToDisplay(models.Model):
    _name = 'config.page.to.display'
    user_id = fields.Many2one('res.users')
    home_page = fields.Boolean(default=False)
    collections = fields.Boolean(default=False)
    product_page = fields.Boolean(default=False)
    cart = fields.Boolean(default=False)
    thank_page = fields.Boolean(default=False)
    blog_post = fields.Boolean(default=False)
    url_ending = fields.Boolean(default=False)
    account_page = fields.Boolean(default=False)

    @api.model
    def create(self, vals):
        res = super(ConfigPageToDisplay, self).create(vals)
        current_id = self.env['res.users'].search([('id', '=', self.env.uid)])
        val = {
            'config_pages_to_display_id': res.id
        }
        res.user_id = current_id.id
        current_id.update(val)
        return res

    def confirm(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'button_template_client_action',
        }
