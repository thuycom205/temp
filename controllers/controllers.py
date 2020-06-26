# -*- coding: utf-8 -*-
from odoo import http, fields
import shopify
from .config import DefaultConfig
from functools import wraps
from flask import session
import werkzeug
from flask import session, redirect, url_for, request, current_app
from functools import partial
import logging
import json

_logger = logging.getLogger(__name__)


def shopify_auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "shopify_token" not in session:
            shop_url = request.args.get('shop')
            shopify.Session.setup(
                api_key=current_app.SHOPIFY_API_KEY,
                secret=current_app.SHOPIFY_SHARED_SECRET)
            try:
                shopify_session = \
                    shopify.Session.validate_params(request.args)
            except Exception as ex:
                return redirect(url_for('shopify_bp.install', **request.args))

            try:
                shop = ' '
                shops = http.request.env['shopify_app.shop'].search([('url', 'like', shop_url)])
                if shops:
                    shop = shops.ids[0];
                    session['shopify_token'] = shop.token
                    session['shopify_url'] = shop_url
                    session['shopify_id'] = shop.id


            #  shop = Shop.query.filter_by(shop=shop_url).one()
            except Exception as ex:
                return redirect(url_for('/shopify_app/shopify_app/', **request.args))



        else:
            try:
                shop = ' '
            # shop = Shop.query.filter_by(shop=session['shopify_url']).one()
            except Exception as ex:
                session.pop("shopify_token")
                session.pop("shopify_url")
                session.pop("shopify_id")
                return redirect(url_for('/shopify_app/shopify_app/', **request.args))

        return f(*args, **kwargs)

    return decorated_function


class ConfigShopifyApp(http.Controller):
    @http.route('/shopify/config/basic', type='http', auth='public', csrf=False)
    def config_basic_form(self, **kwargs):
        user = http.request.env.context.get('uid')
        check_user_config = http.request.env['res.users'].sudo().search([('id', '=', user)])

        if kwargs:
            vals_basic_app = {
                'user_id': user,
                'select_colour': kwargs['background_color_style'],
                'background_colour_1': kwargs['background_color_1'],
                'background_colour_2': kwargs['background_color_2'],
                'icon_colour': kwargs['icon_color'],
                'button_color': kwargs['button_text_color'],
                'chat_button_text': kwargs['chat_button_text'],
                'whatsapp_message_body': kwargs['whatsapp_message_body'],
                'include_url': True if 'include_url' in kwargs else False,
                'show_callout_button': True if 'show_callout_button' in kwargs else False,
                'callout_car_text': kwargs['callout_car_text'],
                'callout_card_delay': kwargs['callout_card_delay'],
                'select_colour_widget': kwargs['select_colour_widget'],
                'background_colour_1_widget': kwargs['background_color_1_widget'],
                'background_colour_2_widget': kwargs['background_color_2_widget'],
                'heading_text_colour': kwargs['heading_text_colour'],
                'description_text_colour': kwargs['description_text_colour'],
                'title_widget': kwargs['title_widget'],
                'help_text': kwargs['help_text'],
                'randomise_order': True if 'randomise_order' in kwargs else False,
                'chat_button_display': kwargs['chat_button_display'],
                'button_mobile_position': kwargs['button_mobile_position'],
                'button_desktop_position': kwargs['button_desktop_position'],
                'height_mobile': kwargs['height_mobile'],
                'height_desktop': kwargs['height_desktop'],
                'edge_mobile': kwargs['edge_mobile'],
                'edge_desktop': kwargs['edge_desktop'],
                # 'set_height_button_page': True if 'set_height_button_page' in kwargs else False,
                # 'height_mobile_page': kwargs['height_mobile_page'],
                # 'height_desktop_page': kwargs['height_desktop_page'],
                'home_page': True if 'home_page' in kwargs else False,
                'collections': True if 'collections' in kwargs else False,
                'product_page': True if 'product_page' in kwargs else False,
                'cart': True if 'cart' in kwargs else False,
                'thank_page': True if 'thank_page' in kwargs else False,
                'blog_post': True if 'blog_post' in kwargs else False,
                'url_ending': True if 'url_ending' in kwargs else False,
                'account_page': True if 'account_page' in kwargs else False
            }
        if check_user_config:
            if not check_user_config.config_basic_id:
                config_create = http.request.env['config.basic.whats.app'].sudo().create(vals_basic_app)
                http.request.env['res.users'].sudo().search([('id', '=', user)]).update({
                    'config_basic_id': config_create
                })
            else:
                config_update = http.request.env['config.basic.whats.app'].sudo().search(
                    [('user_id', '=', user)]).update(vals_basic_app)


class ShopifyApp(http.Controller):
    @http.route('/shopify_app/sync_product/', auth='public')
    def sync_product(self, **kw):
        uid = http.request.httprequest.session.uid
        shopify_token = http.request.httprequest.session.shopify_token
        kargs = {"source_name": "any"}

        http.request.httprequest.session.shopify_token
        http.request.httprequest.session.shop
        shopify_session = http.request.httprequest.session.shopify_obj

        if shopify_session:
            x = 1

            shopify.ShopifyResource.activate_session(shopify_session)

            response_product = shopify.Product.find(tags="rental")
            vals = []
            if response_product:
                for response_product_item in response_product:
                    # shopify.resources.product.Product.attributes
                    item_val = {}
                    shopify_product_id = response_product_item.attributes['id']
                    shopify_product_title = response_product_item.attributes['title']
                    item_val['shopify_product_id'] = shopify_product_id
                    item_val['title'] = shopify_product_title
                    vals.append(item_val)

                    variants = response_product_item.attributes['variants']
                    if variants:
                        for variant in variants:
                            x = variant.attributes['option1']
                            y = variant.attributes['title']
                    options = response_product_item.attributes['options']
                    if options:
                        for option in options:
                            option_name = option.attributes['name']
                            value_list = option.attributes['values']
                # end of for
                http.request.env['rental.shopify_base_product'].create(vals)
            # insert shopify product to database
            output = []
            result = {}
            result['success'] = 'ok'
            output.append(result)
            return output;
        else:
            output = []
            result = {}
            result['success'] = 'ok'
            output.append(result)
            return output;

    @http.route('/shopify_app/test/', auth='public')
    def test(self, **kw):
        # response = shopify.Order.find_first(dict(source_name='web')).reload();
        # x = 1
        # shop1 = http.request.env['shopify_app.shopify_app']
        # shopr = shop1.browse(1)
        # x = 1;
        # shopr.findProductBaseOnTags(5)

        # overwriting
        # end of overwriting
        # http.Root.get_response =  http.Root.get_responsex
        # http.Root.get_response = partial(http.Root, http.Root.get_responsex)

        return http.request.render('shopify_app.listing', {
            'object': 'obj', 'permission_url': 'xyz'
        })

    @http.route('/shopify_app/delete/', auth='public')
    def deleteold(self, **kw):
        organizationEnv = http.request.env['shopify_app.shop']
        organizationEnv.sudo().search([('url', '=', 'closeclose.myshopify.com')]).unlink()

        user = http.request.env['res.users']
        userId = user.sudo().search([("login", "=", 'closeclose@gmail.com')]).unlink()

        return http.request.render('shopify_app.home', {
            'object': 'obj', 'permission_url': 'xyz'
        })

    @http.route('/shopify_app/deletecom/', auth='public')
    def deleteoldcom(self, **kw):

        companyModel = http.request.env['res.company']

        company = companyModel.sudo().search([("name", "=", 'closeclose.myshopify.com')]).unlink()

        return http.request.render('shopify_app.home', {
            'object': 'obj', 'permission_url': 'xyz'
        })

    @http.route('/shopify_app/createshopuser/', auth='public')
    def createshopuser(self, **kw):
        shopUrl = 'closeclose2'
        shopUrlemail = 'closeclose2@gmail.com'
        companyModel = http.request.env['res.company']
        #                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):

        company = companyModel.sudo().search([("name", "=", shopUrl)])
        if not company:
            vals = {'logo': False, 'currency_id': 2, 'sequence': 10,
                    'favicon': 'AAABAAEAEBAAAAAAIAAGAgAAFgAAAIlQTkcNChoKAAAADUlIRFIAAAAQAAAAEAgGAAAAH/P/YQAAAc1JREFUeJyV0s+LzVEYBvDP+53vNUYzSZqFlbBgJUL5tWByJzaysZPJP2AhP+7SYhZXKZEtNRZKlqPUjEQTFmbhH5AosRPjTrr3zvdY3DO6ZiKe09k8z/u85+15T8i4c2xSraiRrBX24ih2YA3e4ileoJVSMjHbAAFT403tTtdgrbYbF3AcG5f1jK+YxbXFpYX5oYFhEzMNMVVvGh4c0mr/OIkb2OrveIfzA0U86i5VyojQav84gFvYnIu+4xXeoMQe7MMQtuDmUpU+R8R8iWFc7jO/x5XEdLAYRaGqqpHgNCaxKU95KaV0rsThHBi00AjxIKmcnekFNVVvLtRqa+52up0CtzGIekQcLHAE63ODl4npSjKRzTAx29DudiQe4nWmN2CsWBHam0K0UqpWR5eSIuIr5vvYbYXfV5VWO5eFtKy2++iiwIc+YmclrYsoVjWICJVqHXb20e8KzOmtDQ4F44F79eavqql6U/TOOA5l+huelYnn0dt5HSNoYjGFp/fGr3Xz+CXGsjaSGzzDXBl8wXXswii2436Ix3LiIfbhhN73ho/Zs1BCSulJRDTyC6O58Ey+K/EJFztL3bmyGBCn9l/9Y/L/gtVx/yd+Akefkiz2xrqJAAAAAElFTkSuQmCC',
                    'rule_type': 'not_synchronize', 'intercompany_user_id': 1, '__last_update': False, 'name': shopUrl,
                    'street': False, 'street2': False, 'city': False, 'state_id': False, 'zip': False,
                    'country_id': False, 'phone': False, 'email': False, 'website': False, 'vat': False,
                    'company_registry': False, 'parent_id': False, 'social_twitter': False, 'social_facebook': False,
                    'social_github': False, 'social_linkedin': False, 'social_youtube': False,
                    'social_instagram': False, 'applicable_on': False, 'warehouse_id': False, 'auto_validation': False}
            companyShop = companyModel.create(vals);
            companyId = companyShop.id

            # create user for the company
            user = http.request.env['res.users']
            #                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):

            userId = user.sudo().search([("login", "=", shopUrlemail)])
            if not userId:
                vals = {'is_published': False, 'company_ids': [[6, False, [companyId]]], 'company_id': companyId,
                        'active': True,
                        'lang': 'en_US', 'tz': 'Europe/Brussels', 'notification_type': 'email',
                        'odoobot_state': 'not_initialized', 'image_1920': False, '__last_update': False,
                        'name': shopUrl, 'email': shopUrlemail, 'login': shopUrlemail,
                        'password': '123123', 'action_id': False, 'alias_id': False, 'alias_contact': False,
                        'signature': '<p><br></p>', 'sign_signature': False, 'sign_initials': False,
                        'livechat_username': False, 'groups_id': [(6, 0,
                                                                   [1, 40, 31])]};
                createdUser = user.sudo().create(vals);
                createdUserId = createdUser.id
                x = 123
            # create organization for shop
            organizationEnv = http.request.env['shopify_app.shop']
            organization = organizationEnv.sudo().search([("code", "=", shopUrl)])
            if not organization:
                vals = {
                    'url': shopUrl,
                    'code': shopUrl}

                createdOrg = organization.sudo().create(vals)
                createOrgId = createdOrg.id
                # update organization id for the created user
                createdUser.sudo().write({'org_id': createOrgId})

    @http.route('/shopify_app/indexy/', auth='public')
    def homea(self, **kw):
        # session = shopify.Session('https://closeclose.myshopify.com/', 'unstable')
        db = http.request.env.cr.dbname;
        uid = http.request.session.authenticate(db, "closefirst2@gmail.com", "123123")
        return http.request.render('shopify_app.home', {
            'object': 'obj', 'permission_url': 'xyz'
        })

    @http.route('/shopify_app/indexx/', auth='public')
    def homeb(self, **kw):
        # session = shopify.Session('https://closeclose.myshopify.com/', 'unstable')
        h = http.request.httprequest.session
        return http.request.render('shopify_app.home', {
            'object': 'obj', 'permission_url': 'xyz'
        })

    @http.route('/shopify_app/plan/', auth='public')
    def plan(self, **kw):
        return werkzeug.utils.redirect(
            'https://44ca288ecea5.ngrok.io/web#action=1096&model=sale.order&view_type=kanban&cids=19&menu_id=781')

    # shopify_app / app_uninstalled
    @http.route('/shopify_app/order_create', type='json', auth='public')
    def order_create(self, **kwargs):
        y = kwargs;
        h = http.request.httprequest;
        data = h.data
        encoding = 'utf-8'
        paypload = str(data, encoding)
        orderItem = json.loads(paypload)  # obj now contains a dict of the data
        is_rent_ok = False
        odooOrderLine = []
        orderId = orderItem['id'];
        orderItem['email'];
        orderItem['created_at'];
        # '2020-04-07T22:26:27-04:00'
        orderItem['number'];
        # int 1
        orderItem['gateway'];
        orderItem['total_price'];
        # total price is string
        orderItem['subtotal_price'];
        orderItem['total_tax'];
        orderItem['currency'];
        orderItem['confirmed'];
        # confirm is Boolean
        orderItem['total_discounts'];
        orderItem['cart_token'];
        orderItem['name'];
        # name is increment id #1001
        orderItem['cancelled_at'];
        # cancelled at is None perhaps
        orderItem['cancel_reason'];
        # none
        orderItem['total_price_usd'];
        # string
        orderItem['checkout_token'];
        orderItem['customer_locale'];

        order_line = []
        listLineItems = orderItem['line_items']
        for lineItem in listLineItems:
            orderLineTuple = ()
            lineitemId = lineItem['id']
            lineItemVariantId = lineItem['variant_id']
            productIdLineItemVariant = lineItem['product_id']
            # Cup - 1/s
            lineItemName = lineItem['name']
            orderLineProductName = lineItemName
            if '-' in lineItemName:
                orderLineProductName = lineItemName.split('-')[0]

            # int
            fulfillable_quantity = lineItem['fulfillable_quantity']
            # string 700
            price = lineItem['price']
            properties = lineItem['properties']
            if properties:
                for property in properties:
                    # From or To
                    pName = property['name']

                    # 2020-04-15
                    pValue = property['value']
                    if 'From' in pName or "FROM" in pName:
                        is_rent_ok = True
            # create t
            product = http.request.env['product.template']
            productVariant = http.request.env['product.product']

            productInOdoo = product.sudo().search([('name', 'ilike', '%' + orderLineProductName.rstrip() + '%')],
                                                  limit=1)

            if productInOdoo:
                productId = productInOdoo.id
                productVariantObj = productVariant.sudo().search([('product_tmpl_id', '=', productInOdoo.id)], limit=1)
                # else:
                #     x = 1
                #     # create the product in Odoo
                orderLineTuple = (0, 0, {
                    'product_uom_qty': fulfillable_quantity,
                    'product_id': productVariantObj.id,
                    'product_template_id': productId})

            odooOrderLine.append(orderLineTuple)

        # parse customer
        sCustomer = orderItem['customer']
        # int
        sCustomerId = sCustomer['id']
        sCustomerEmail = sCustomer['email']
        sCustomerFirstName = sCustomer['first_name']
        sCustomerLastName = sCustomer['last_name']

        customerDefaultAddress = sCustomer['default_address']
        sCustomerAddr1 = customerDefaultAddress['address1']
        sCustomerAddr2 = customerDefaultAddress['address2']
        sCustomerAddrCity = customerDefaultAddress['city']
        sCustomerAddrProvince = customerDefaultAddress['province']
        sCustomezip = customerDefaultAddress['zip']
        sCustomeAddrName = customerDefaultAddress['name']
        sCustomerAddrPhone = customerDefaultAddress['phone']
        sCustomerAddrCountryCode = customerDefaultAddress['country_code']
        sCustomerAddrCountryName = customerDefaultAddress['country_name']

        partner = http.request.env['res.partner']
        customer = partner.sudo().search([('email', '=', sCustomerEmail)], limit=1)

        customerId = 0
        if customer:
            customerObj = partner.browse([customer.id])
            customerId = customerObj.id
        else:
            val = {
                'name': kwargs['name'] if 'name' in kwargs else False,
                'company_type': 'person',
                'street': kwargs['street1'] if 'street1' in kwargs else False,
                'street2': kwargs['street2'] if 'street2' in kwargs else False,
                'city': kwargs['city'] if 'city' in kwargs else False,
                'zip': kwargs['zip'] if 'zip' in kwargs else False,
                # 203
                'state_id': kwargs['state_id'] if 'state_id' in kwargs else False,
                # 113
                'country_id': kwargs['country_id'] if 'country_id' in kwargs else False,
                'phone': kwargs['phone'] if 'phone' in kwargs else False,
                'email': kwargs['email'] if 'email' in kwargs else False,
                'type': 'delivery'
            }
            customerObj = partner.sudo().create(val)
            customerId = customerObj.id

        order = http.request.env['sale.order']
        vals = {
            'is_rental_order': 'true',
            'date_order': '2020-04-11 14:04:28',
            'state': 'sale',
            'date_order': fields.Datetime.now(),
            'partner_id': customerId,
            'order_line': odooOrderLine
        }

        z = 1

        #createdOrder = order.sudo().create(vals)
        # Them order shopify vao database
        vals_shopify_order = {
            'checkout_user': str(orderItem['name']) + ' : ' + str(orderItem['checkout_id']),
            'date': orderItem['created_at'],
            'amount': orderItem['total_price'],
            'status': 'Online'
        }
        http.request.env['config.manual.order.crm.line'].sudo().create(vals_shopify_order)
        # end customer
        # _logger.debug(" ========>order: %s !", (obj))

    @http.route('/shopify_app/home/', auth='public')
    def home(self, **kw):
        h = http.request.httprequest.session
        uid = http.request.httprequest.session.uid
        shopify_token = http.request.httprequest.session.shopify_token
        kargs = {"source_name": "any"}

        http.request.httprequest.session.shopify_token
        http.request.httprequest.session.shop
        shopify_session = http.request.httprequest.session.shopify_obj
        x = shopify.ShopifyResource
        x = 2
        if shopify_session != None:
            shopify.ShopifyResource.activate_session(shopify_session)
            response = shopify.Order.find(status="open")
            response_product = shopify.Product.find(tags="rental")
            x = 1

        if uid and shopify_token:
            return werkzeug.utils.redirect(
                'https://44ca288ecea5.ngrok.io/web#action=1096&model=sale.order&view_type=kanban&cids=19&menu_id=781')

            # return http.request.render('shopify_app.plan', {
            #     'object': 'obj', 'permission_url': 'xyz'
            # })
        ##################
        db = http.request.env.cr.dbname;
        if not http.request.httprequest.session.uid:
            x = 3
            token = http.request.httprequest.session.shopify_token
            shopUrlemail = http.request.httprequest.session.shopify_email

            # fix me =
            shopUrlemail = 'storeodoo@gmail.com'
            x = 4
            uid = http.request.httprequest.session.authenticate(db, shopUrlemail, "token")
            y = uid
            return werkzeug.utils.redirect('https://44ca288ecea5.ngrok.io/web#action=1096&model=sale.order&view_type'
                                           '=kanban&cids=19&menu_id=781')
        # session = shopify.Session('https://closeclose.myshopify.com/', 'unstable')
        #  user = http.request.env['res.users']
        # #                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):
        #
        #  userId = user.sudo().search([("login","=", "closefirst2@gmail.com")])
        #  if not userId :
        #     vals={'is_published': False, 'company_ids': [[6, False, [2]]], 'company_id': 2, 'active': True, 'lang': 'en_US', 'tz': 'Europe/Brussels', 'notification_type': 'email', 'odoobot_state': 'not_initialized', 'image_1920': False, '__last_update': False, 'name': 'closefirst', 'email': 'closefirst@gmail.com', 'login': 'closefirst2@gmail.com', 'password': '123123','action_id': False, 'alias_id': False, 'alias_contact': False, 'signature': '<p><br></p>', 'sign_signature': False, 'sign_initials': False, 'livechat_username': False, 'groups_id': [(6, 0, [1, 33, 83, 87, 44, 38, 99, 72, 62, 65, 63, 85, 93, 74, 67, 101, 47, 22, 110, 77, 69, 121, 116, 105, 120, 51, 88, 97, 41, 55, 15, 36, 12, 13, 28, 111, 56, 14, 18, 24, 60, 54, 23, 19, 11, 20, 25, 16, 17, 26, 52, 108, 39, 53, 58, 45, 70, 30, 49, 48, 7, 5, 6, 10, 32, 29, 82, 81, 86, 40, 43, 42, 115, 21, 37, 98, 100, 71, 61, 64, 84, 119, 94, 92, 73, 66, 46, 109, 68, 50, 96])]};
        #     user.create(vals);
        else:
            return werkzeug.utils.redirect('https://44ca288ecea5.ngrok.io/web#action=1096&model=sale.order&view_type'
                                           '=kanban&cids=19&menu_id=781')

    @http.route('/shopify_app/shopify_app/', auth='public')
    def index(self, **kw):
        shopify.ShopifyResource.clear_session()

        _env = http.request.env
        shop_url = kw['shop']
        current_app = DefaultConfig()
        shopify.Session.setup(
            api_key=current_app.SHOPIFY_API_KEY,
            secret=current_app.SHOPIFY_SHARED_SECRET)

        session = shopify.Session(shop_url, 'unstable')

        scope = [
            "write_products", "read_products", "read_script_tags",
            "write_script_tags", "read_orders", "write_orders"]
        redirect_uri = "https://44ca288ecea5.ngrok.io/shopify_app/finalize"
        permission_url = session.create_permission_url(
            scope, redirect_uri)
        return werkzeug.utils.redirect(permission_url)

    @http.route('/shopify_app/finalize/', auth='public')
    def finalize(self, **kw):
        shop_url = kw['shop']
        current_app = DefaultConfig()

        shopify.Session.setup(
            api_key=current_app.SHOPIFY_API_KEY,
            secret=current_app.SHOPIFY_SHARED_SECRET)
        shopify_session = shopify.Session(shop_url, 'unstable')
        http.request.httprequest.session.shopify_obj = shopify_session
        token = shopify_session.request_token(kw)

        organizationEnv = http.request.env['shopify_app.shop']
        organization = organizationEnv.sudo().search([("url", "=", shop_url)])
        if not organization:
            vals = {
                'url': shop_url,
                'code': token}

            createdOrg = organization.sudo().create(vals)

            # Create company
            shopUrl = shop_url
            shopUrlemail = shop_url.split('.')[0] + '@gmail.com'
            companyModel = http.request.env['res.company']
            # if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):

            company = companyModel.sudo().search([("name", "=", shopUrl)])
            if not company:
                vals = {'logo': False, 'currency_id': 2, 'sequence': 10,
                        'favicon': 'AAABAAEAEBAAAAAAIAAGAgAAFgAAAIlQTkcNChoKAAAADUlIRFIAAAAQAAAAEAgGAAAAH/P/YQAAAc1JREFUeJyV0s+LzVEYBvDP+53vNUYzSZqFlbBgJUL5tWByJzaysZPJP2AhP+7SYhZXKZEtNRZKlqPUjEQTFmbhH5AosRPjTrr3zvdY3DO6ZiKe09k8z/u85+15T8i4c2xSraiRrBX24ih2YA3e4ileoJVSMjHbAAFT403tTtdgrbYbF3AcG5f1jK+YxbXFpYX5oYFhEzMNMVVvGh4c0mr/OIkb2OrveIfzA0U86i5VyojQav84gFvYnIu+4xXeoMQe7MMQtuDmUpU+R8R8iWFc7jO/x5XEdLAYRaGqqpHgNCaxKU95KaV0rsThHBi00AjxIKmcnekFNVVvLtRqa+52up0CtzGIekQcLHAE63ODl4npSjKRzTAx29DudiQe4nWmN2CsWBHam0K0UqpWR5eSIuIr5vvYbYXfV5VWO5eFtKy2++iiwIc+YmclrYsoVjWICJVqHXb20e8KzOmtDQ4F44F79eavqql6U/TOOA5l+huelYnn0dt5HSNoYjGFp/fGr3Xz+CXGsjaSGzzDXBl8wXXswii2436Ix3LiIfbhhN73ho/Zs1BCSulJRDTyC6O58Ey+K/EJFztL3bmyGBCn9l/9Y/L/gtVx/yd+Akefkiz2xrqJAAAAAElFTkSuQmCC',
                        'name': shopUrl, 'street': False, 'street2': False, 'city': False, 'state_id': False,
                        'zip': False, 'country_id': False, 'phone': False, 'email': False, 'website': False,
                        'vat': False, 'company_registry': False, 'parent_id': False}
                companyShop = companyModel.sudo().create(vals);
                companyId = companyShop.id
                # create User ID
                # create user for the company
                user = http.request.env['res.users']
                #                if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):

                userId = user.sudo().search([("login", "=", shopUrlemail)])
                if not userId:
                    vals = {'is_published': False, 'company_ids': [[6, False, [companyId]]], 'company_id': companyId,
                            'active': True,
                            'lang': 'en_US', 'tz': 'Europe/Brussels', 'notification_type': 'email',
                            'odoobot_state': 'not_initialized', 'image_1920': False, '__last_update': False,
                            'name': shopUrl, 'email': shopUrlemail, 'login': shopUrlemail,
                            'password': 'token', 'action_id': False, 'alias_id': False, 'alias_contact': False,
                            'groups_id': [(6, 0,
                                           [1])]};
                    createdUser = user.sudo().create(vals);
                    createdUserId = createdUser.id
                    # db = http.request.env.cr.dbname;
                    # uid = http.request.httprequest.session.authenticate(db, shopUrlemail, "token")
                    http.request.httprequest.session.shopify_token = token
                    http.request.httprequest.session.shopify_email = shopUrlemail

                    shopify.ShopifyResource.activate_session(shopify_session)
                    scrpt = shopify.ScriptTag(
                        dict(event='onload',
                             src="https://44ca288ecea5.ngrok.io/shopify_app/static/src/js/shopify.js")).save()

                    # order create webhook
                    weekhooks_response = shopify.Webhook(dict(topic="orders/create",
                                                              address="https://44ca288ecea5.ngrok.io/shopify_app/order_create",
                                                              format="json")).save()
                    # uninstall app webhook
                    weekhooks_uninstall_response = shopify.Webhook(dict(topic="app/uninstalled",
                                                                        address="https://44ca288ecea5.ngrok.io/shopify_app/app_uninstalled",
                                                                        format="json")).save()
                    x = 1
            else:
                # never run into this block of code
                user = http.request.env['res.users']
                companyId = company.id
                userId = user.sudo().search([("login", "=", shopUrlemail)])
                if not userId:
                    vals = {'is_published': False, 'company_ids': [[6, False, [companyId]]], 'company_id': companyId,
                            'active': True,
                            'lang': 'en_US', 'tz': 'Europe/Brussels', 'notification_type': 'email',
                            'odoobot_state': 'not_initialized', 'image_1920': False, '__last_update': False,
                            'name': shopUrl, 'email': shopUrlemail, 'login': shopUrlemail,
                            'password': 'token', 'action_id': False, 'alias_id': False, 'alias_contact': False,
                            'signature': '<p><br></p>', 'sign_signature': False, 'sign_initials': False,
                            'livechat_username': False, 'groups_id': [(6, 0,
                                                                       [1, 40, 31])]};
                    createdUser = user.sudo().create(vals);
                    createdUserId = createdUser.id
                    # db = http.request.env.cr.dbname;
                    # uid = http.request.httprequest.session.authenticate(db, shopUrlemail, "token")
                    http.request.httprequest.session.shopify_token = token
                    http.request.httprequest.session.shopify_email = shopUrlemail

                    shopify.ShopifyResource.activate_session(shopify_session)
                    scrpt = shopify.ScriptTag(
                        dict(event='onload',
                             src="https://44ca288ecea5.ngrok.io/shopify_app/static/src/js/shopify.js")).save()

                    weekhooks_response = shopify.Webhook(dict(topic="orders/create",
                                                              address="https://44ca288ecea5.ngrok.io/shopify_app/order_create",
                                                              format="json")).save()

                    response = shopify.Order.find_first(source_name="web");

                    x = 1


        else:
            organizationId = organization.id

            firstStoredToken = organization.code
            organization.write({'code': token})
            user = http.request.env['res.users']

            shopUrlemail = shop_url.split('.')[0] + '@gmail.com'
            user = user.sudo().search([("login", "=", shopUrlemail)])

            shopUrlemail = shop_url.split('.')[0] + '@gmail.com'
            http.request.httprequest.session.shopify_email = shopUrlemail

            if user:
                db = http.request.env.cr.dbname;
                uid = http.request.httprequest.session.authenticate(db, shopUrlemail, 'token')
                http.request.httprequest.session.shopify_token = token
                shopify.ShopifyResource.activate_session(shopify_session)
                scrpt = shopify.ScriptTag(
                    dict(event='onload',
                         src="https://44ca288ecea5.ngrok.io/shopify_app/static/src/js/shopify.js")).save()

                weekhooks_response = shopify.Webhook(dict(topic="orders/create",
                                                          address="https://44ca288ecea5.ngrok.io/shopify_app/order_create",
                                                          format="json")).save()

                response = shopify.Order.find_first(source_name="web");

                x = 1

        redirect = werkzeug.utils.redirect('/shopify_app/home')

        return redirect
