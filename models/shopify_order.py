from odoo import models, fields, api


class shopify_order(models.Model):
    _name = 'shopify_app.shopify_base_order'
    _description = 'Shopify order'

    name = fields.Char()
    title = fields.Char()
    order_id = fields.Float()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

    # def createRentalOrder(self,**kwargs):
    #     partner = self.env['res.partner']
    #
    #     val = {
    #         'name': kwargs['name'],
    #         'company_type' : 'person',
    #         'street' : kwargs['street1'],
    #         'stree2' : kwargs['street2'] ,
    #         'city' : kwargs['city'],
    #         'zip' : kwargs['zip'],
    #         # 203
    #         'state_id' :kwargs['state_id'],
    #         # 113
    #         'country_id' : kwargs['country_id'],
    #         'phone' : kwargs['phone'],
    #         'email' : kwargs['email'],
    #         'type' : 'delivery'
    #      }
    #     obj = partner.sudo().create(val)
    #     objId = obj.id
    #     order = self.env['sale.order']
    #     vals = {
    #         'is_rental_order' : 'true',
    #     'date_order' :'2020-04-11 14:04:28',
    #         'partner_id' : objId,
    #         'order_line' : [0, 0 , {
    #             'product_uom_qty' : 1,
    #             'product_id' : 31,
    #             'product_template_id' : 23
    #         }]
    #
    #     }
    #     order.sudo().create(vals)
    # create new rental order
