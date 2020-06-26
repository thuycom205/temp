odoo.define('rental.RentalOrderListView', function (require) {
"use strict";

var ListView = require('web.ListView');
var RentalOrderListController = require('rental.RentalOrderListController');
var viewRegistry = require('web.view_registry');


var RentalOrderListView = ListView.extend({
    config: _.extend({}, ListView.prototype.config, {
        Controller: RentalOrderListController,
    }),
});

viewRegistry.add('rental_order_list', RentalOrderListView);

return RentalOrderListView;

});
