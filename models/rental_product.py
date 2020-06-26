from odoo import models, api,fields
from odoo.osv import expression
import json
import logging

_logger = logging.getLogger(__name__)

class ShopifyRentalProduct(models.TransientModel):
    _name = "rental.shopify_base_product"
    _description = "Account Unreconcile"
    shopify_product_id = fields.Float()
    title = fields.Text()

    # @api.model


    @api.model
    @api.depends('name', 'title')
    def name_get(self):
        result = []
        for rec in self:
            name =  str(rec.title)
            result.append((rec.id, name))
        return result
    # def name_get(self):
    #     result = []
    #     for bank in self:
    #         val = {}
    #         name = bank.title
    #
    #         val['name'] = name
    #         result.append(val)
    #     return result
    @api.model
    def synch_product(self):
         x = 11

class ShopifyRentalProduct(models.TransientModel):
    _name = "rental.shopify_product"
    _description = "Rental product"

    product_id = fields.Many2one('rental.shopify_base_product',  'Product')
    rental_pricing_ids  = fields.One2many(
        'shopify.rental.pricing', 'product_template_id',
        string="Rental Pricings", auto_join=True, copy=True)

    shopify_product_id = fields.Float()
    shopify_product_title = fields.Text()

    is_Edit = fields.Boolean('isEdit', default=False)
    edit_id = fields.Integer('edit_id')

    def next_step(self):
        x = 1
        # y = self.title
        productName = self.product_id.title
        shopify_product_id = self.product_id.shopify_product_id
        pricing_ids  = self.rental_pricing_ids

        pricing_list = []

        if pricing_ids:
            for pricing_id in pricing_ids:
                pricing_dic = {}
                duration = pricing_id['duration']
                pricing_dic['duration'] = duration

                unit = pricing_id['unit']
                pricing_dic['unit'] = unit

                price = pricing_id['price']
                pricing_dic['price'] = price
                tuplePrice = (0,0,pricing_dic)
                pricing_list.append(tuplePrice)

        # self.write(self)
        if  not self.is_Edit:
            x = 1
            self.createRentalProduct(product_name= productName,shopify_product_id = shopify_product_id, pricing = pricing_list)
        else:
            x =1
            self.createRentalProduct(product_name= productName,shopify_product_id = shopify_product_id, pricing = pricing_list)



    @api.onchange('product_id')
    def _onchange_product_id(self):
        """Clean rental related data if new product cannot be rented."""
        if not self.product_id:
            return
        else :
            thisid = self.search([
                ('product_id', '=', self.product_id.id),

            ], order='id', limit=1)
            # return {
            #     'type': 'ir.actions.act_window',
            #     'res_model': 'rental.shopify_product',
            #     'views': [[False, 'form']],
            #     'res_id': thisid.id,
            # }


        self.update({
                'is_Edit' : True,
                'edit_id' : thisid.id,
                'shopify_product_title': self.product_id.title,
                'rental_pricing_ids' : thisid.rental_pricing_ids

            })

    # @api.model
    # def create(self, values):
    #     x=1
    #     if values['is_Edit'] :
    #         x = 2
    #         if values['is_Edit'] == True:
    #             editId = values['edit_id']
    #             theEditObj = self.browse([editId])
    #             values['id'] = theEditObj.id
    #             theEditObj.unlink()
    #     super(ShopifyRentalProduct,self).create(values)



    def  action_create_product(self):
        x = 11
        self.createRentalProduct(product_name= 'black mini dress')

    def createRentalProduct(self,**kwargs):
        val = {
            'name' : kwargs['product_name'],
            'rent_ok' : True,
            'active' : True,
            'type' : 'product',
            'rental_pricing_ids':kwargs['pricing']
        }

        productTemplate = self.env['product.template']

        # check if the shopify product id already existed

        shopify_product_id = kwargs['shopify_product_id']
        product = productTemplate.search([
                ('shopify_product_id', '=', shopify_product_id),

            ], order='id', limit=1)

        if product:
            productOb = productTemplate.browse([product.id])
            productOb.write(val)
        else :
            productTemplate.sudo().create(val)

    def action_move_line_select(self):
         x = 11
         self.createRentalOrder(name = 'Mac', street1 = 'street', street2 = 'street2' , city ='Hanoi' , zip = '100000',
                                state_id = 203,country_id=113,phone='09866',email = 'thuyduong@gmail.com'
                                )
         x = 2
    def createRentalOrder(self,**kwargs):
        _logger.debug(" ========>: %s !", (kwargs))

        partner = self.env['res.partner']

        val = {
            'name': kwargs['name'],
            'company_type' : 'person',
            'street' : kwargs['street1'],
            'street2' : kwargs['street2'] ,
            'city' : kwargs['city'],
            'zip' : kwargs['zip'],
            # 203
            'state_id' :kwargs['state_id'],
            # 113
            'country_id' : kwargs['country_id'],
            'phone' : kwargs['phone'],
            'email' : kwargs['email'],
            'type' : 'delivery'
         }
        obj = partner.sudo().create(val)
        objId = obj.id
        order = self.env['sale.order']
        vals = {
            'is_rental_order' : 'true',
            'date_order' :'2020-04-11 14:04:28',
            'state': 'sale',
            'date_order': fields.Datetime.now(),
            'partner_id' : objId,
            'order_line' : [(0, 0 , {
                'product_uom_qty' : 1,
                'product_id' : 31,
                'product_template_id' : 23
            })]

        }
        order.sudo().create(vals)



class ShopifyRentalPricing(models.TransientModel):

    _name = 'shopify.rental.pricing'
    _description = 'Pricing rule of rentals'
    _order = 'price'

    duration = fields.Integer(
        string="Duration", required=True,
        help="Minimum duration before this rule is applied. If set to 0, it represents a fixed rental price.")
    unit = fields.Selection([("hour", "Hours"), ("day", "Days"), ("week", "Weeks"), ("month", "Months")], string="Unit", required=True, default='day')

    price = fields.Monetary(string="Price", required=True, digits='Product Price', default=1.0)

    product_template_id = fields.Many2one(
        'rental.shopify_product', string="Product Templates",
        help="Select products on which this pricing will be applied.")
    currency_id = fields.Many2one(
        'res.currency', 'Currency',
        default=lambda self: self.env.company.currency_id.id,
        required=True)



# class AccountUnreconcile(models.TransientModel):
#     _name = "rental.shopify_product"
#     _description = "Account Unreconcile"
#     product_id = fields.Many2one('product.product', 'Product', required=True)
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
#
#     def trans_unrec(self):
#         context = dict(self._context or {})
#         if context.get('active_ids', False):
#             self.env['account.move.line'].browse(context.get('active_ids')).remove_move_reconcile()
#         return {'type': 'ir.actions.act_window_close'}
