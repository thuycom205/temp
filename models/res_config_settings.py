# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # RENTAL company defaults :

    # Extra Costs

    rental_from_label = fields.Text('From label')
    rental_to_label = fields.Text('To label')

    @api.onchange('rental_from_label')
    def _onchange_rental_from_label(self):
        properties = self.env['ir.property'].search([('name', '=', 'rental_from_label')])
        if properties:
            properties.write({'value': self.rental_from_label})

    @api.onchange('rental_to_label')
    def _onchange_rental_to_label(self):
        properties = self.env['ir.property'].search([('name', '=', 'rental_to_label')])
        if properties:
            properties.write({'value': self.rental_to_label})
