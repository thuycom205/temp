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
    field_registry.add('link_shopify_product', linkProductShopify);
});
odoo.define('whatsapp.sendmessage.abandoned_cart', function (require) {
    "use strict";
    var AbstractField = require('web.AbstractField');
    var field_registry = require('web.field_registry');

    var sendMessage = AbstractField.extend({
        _render: function () {
            if (this.value) {
                if (this.value == undefined || this.value == null || this.value ==' ')
                {
                    this.$el.html('<span class="open-link-icon">  ' + 'Phone Unavailable' + '</span>');
                } else {

                 var res = this.value.replace(/\+/g, "").replace(/([\(\)])/g, "").replace(/\-/g, "").replace(/^[0]{1,}/g, "");
                   var encodeText = encodeURI('Hello Work pls viet');
                   var encodeText = 'Hello Work pls viet https://api.whatsapp.com/send?phone=849737861238888';
                   //https://api.whatsapp.com/send?phone=84973786123&text=ggggg&source=&data=&app_absent=
                   //window.shopify_store_url  = 'https://wa.me/' + res + '&text=' + encodeText;
                   window.shopify_store_url  = 'https://api.whatsapp.com/send?phone=84973786123/'  + '&text=' + encodeText;
                   this.$el.html('<a href="' + window.shopify_store_url + '" target="_blank"><span class="open-link-icon">  ' + this.value + '</span></a>');
                }

            }
        }
    });
    field_registry.add('whatsapp_sendmessage_abandoned_cart', sendMessage);
});
