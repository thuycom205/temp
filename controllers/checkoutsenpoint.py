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
from odoo.http import request
class OnboardingController(http.Controller):
    @http.route('/whatsapp/abandoned_cart_onboarding_panel/', type='json', auth='user')
    def abandoned_cart_onboarding_panel(self,**kwargs):
        """ Returns the `banner` for the sale onboarding panel.
                    It can be empty if the user has closed it or if he doesn't have
                    the permission to see it. """

        # company = request.env.company
        # if not request.env.is_admin() or \
        #         company.sale_quotation_onboarding_state == 'closed':
        #     return {}
        x =1
        ob = request.env.ref('whatsapp.whatsapp_abandoned_cart_onboarding_panel')
        html = ob.render({
                'company': 'company',
            })

        return {
            'html': html
        }


    @http.route('/shopify_app/checkouts_create/', type='json', auth='public',csrf=False, cors='*')
    def sync_checkouts_create(self,**kwargs):
        httprequest = http.request.httprequest;
        data = httprequest.data
        encoding = 'utf-8'
        paypload = str(data, encoding)
        checkoutData = json.loads(paypload)
        id = checkoutData.attributes['id']
        email = checkoutData.attributes['email']
        #total_price
        # abandoned_checkout_url
        # buyer_accepts_marketing True,False
        # created_at
        # updated_at
        #currency
        # customer_locale
        x =1

    @http.route('/shopify_app/checkouts_update/', type='json', auth='public',csrf=False, cors='*')
    def sync_checkouts_update(self,**kwargs):
        httprequest = http.request.httprequest;
        data = httprequest.data
        encoding = 'utf-8'
        paypload = str(data, encoding)
        orderData = json.loads(paypload)
        x =1

    @http.route('/shopify_app/checkouts_delete/', type='json', auth='public',csrf=False, cors='*')
    def sync_checkouts_delete(self,**kwargs):
        httprequest = http.request.httprequest;
        data = httprequest.data
        encoding = 'utf-8'
        paypload = str(data, encoding)
        orderData = json.loads(paypload)
        x =1



