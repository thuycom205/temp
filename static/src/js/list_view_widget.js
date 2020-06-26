odoo.define('web.link_shopify_order', function (require) {
    "use strict";
    var AbstractField = require('web.AbstractField');
    var field_registry = require('web.field_registry');

    var LinkShopify = AbstractField.extend({
        _render: function () {
            if (this.value) {
                window.shopify_store_url  = 'https://google.com';
                var shopify_order_link =window.shopify_store_url + '/admin/orders/' + this.value;
                console.log(shopify_order_link);
                this.$el.html('<a href="' + shopify_order_link + '" target="_blank"><span class="open-link-icon">  ' + this.value + '</span></a>');
            }
        }
    });
    field_registry.add('link_shopify_order', LinkShopify);
});
odoo.define('web.link_shopify_product', function (require) {
    "use strict";
    var AbstractField = require('web.AbstractField');
    var field_registry = require('web.field_registry');

    var linkProductShopify = AbstractField.extend({
        _render: function () {
            if (this.value) {
                window.shopify_store_url  = 'https://google.com';
                var shopify_product_link =window.shopify_store_url + '/admin/products/' + this.value;
                this.$el.html('<a href="' + shopify_product_link + '" target="_blank"><span class="open-link-icon">  ' + this.value + '</span></a>');
            }
        }
    });
    field_registry.add('link_shopify_order', linkProductShopify);
});
