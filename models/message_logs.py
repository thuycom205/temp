from odoo import models, fields


class MessageLogs(models.Model):
    _name = 'message.logs'
    _rec_name = 'checkout'
    # message_id = fields.Many2one('config.shopify')

    checkout = fields.Char(string='Checkout')
    date = fields.Date(string='Date')
    partner_name = fields.Many2one('res.users', string='Name')
    amount = fields.Char(sring='Amount')
    status = fields.Char(string='Status')
    message = fields.Text(string='Message')





