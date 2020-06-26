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
class ShopifyApp(http.Controller):
    @http.route('/shopify_app/order_create/', type='json', auth='public',csrf=False, cors='*')
    def sync_order_create(self,**kwargs):
        httprequest = http.request.httprequest;
        data = httprequest.data
        encoding = 'utf-8'
        paypload = str(data, encoding)
        orderData = json.loads(paypload)
        x =1

    @http.route('/shopify_app/order_update/', type='json', auth='public',csrf=False, cors='*')
    def sync_order_update(self,**kwargs):
        httprequest = http.request.httprequest;
        data = httprequest.data
        encoding = 'utf-8'
        paypload = str(data, encoding)
        orderData = json.loads(paypload)
        x =1

    @http.route('/shopify_app/order_delete/', type='json', auth='public',csrf=False, cors='*')
    def sync_order_delete(self,**kwargs):
        httprequest = http.request.httprequest;
        data = httprequest.data
        encoding = 'utf-8'
        paypload = str(data, encoding)
        orderData = json.loads(paypload)
        x =1
