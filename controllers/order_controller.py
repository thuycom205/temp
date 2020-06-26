from odoo import http
import shopify
from .config import DefaultConfig
from functools import wraps
from flask import session
import werkzeug
from flask import session, redirect, url_for, request, current_app
from functools import partial
class ShopifyAppDemo(http.Controller):
    @http.route('/shopify_app/sync_order/', auth='public')
    def test(self, **kw):
        shop1 = http.request.env['shopify_app.shopify_app']
        shopr = shop1.browse(1)
        x = 1;
        shopr.findProductBaseOnTags(5)

        #overwriting
        #end of overwriting
        http.Root.get_response =  http.Root.get_responsex
       # http.Root.get_response = partial(http.Root, http.Root.get_responsex)

        return http.request.render('shopify_app.home', {
            'object': 'obj','permission_url':'xyz'
        })