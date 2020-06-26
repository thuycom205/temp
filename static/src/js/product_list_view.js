odoo.define('rental.product.tree', function (require) {
"use strict";
    var core = require('web.core');
    var ListController = require('web.ListController');
    var ListView = require('web.ListView');
    var UploadBillMixin = require('account.upload.bill.mixin');
    var viewRegistry = require('web.view_registry');
    var rpc = require('web.rpc');

    var BillsListController = ListController.extend( {
        buttons_template: 'RentalProductListView.buttons',
        events: _.extend({}, ListController.prototype.events, {
            'click .o_button_wizard': '_onWizard',
        }),
    });



    var KanbanController = require("web.KanbanController");
    var ListController = require("web.ListController");

    var includeDict = {
         events: _.extend({}, ListController.prototype.events, {
            'click .o_list_button_wizard': '_onWizard',
        }),
        _onWizard: function () {
             var bt = this.$buttons;
             if (this.$button != undefined )
             {
                 this.$buttons.append('<span> Loading</span>');

             }

             var self = this;
             ///shopify_app/sync_product/
                return  $.ajax({
                type: "POST",
                url: "/shopify_app/sync_product/",
                async: false,
                data: JSON.stringify({ name: "Shopify"}),


                contentType: "application/json",
                complete: function (data) {
                      var x = data;
                      self.do_action({
                        type: 'ir.actions.act_window',
                        res_model: 'rental.shopify_product',
                        views: [[false, 'form']],
                        target: 'new'
                      });

                },
                error: function () {
                    alert("Error")
                }
            });

            //  rpc.query({
            //       model: 'sale.order',
            //       method: 'search_read',
            //       args: [
            //         [['user_id', '=', [10]]],
            //         ['id', 'name',  'partner_id'],
            //         ]
            //      })
            // .then(function (items){
            //           self.do_action({
            //             type: 'ir.actions.act_window',
            //             res_model: 'rental.shopify_product',
            //             views: [[false, 'form']],
            //             target: 'new'
            //           });
            // });

        },
        renderButtons: function () {
            this._super.apply(this, arguments);
            if (this.$buttons != undefined )

            this.$buttons.append('<button id="wiz" class="btn btn-primary o_list_button_wizard"> Wizard</button>');
            if (this.modelName === "account.bank.statement") {
                var data = this.model.get(this.handle);
                if (data.context.journal_type !== 'cash') {
                    this.$buttons.find('button.o_button_import').hide();
                }
            }
            // setTimeout(function(){
            //     jQuery('#wiz').click(function () {
            //     ListView.do_action({
            // type: 'ir.actions.act_window',
            // res_model: 'account.reconcile.model',
            // views: [[false, 'form']],
            // target: 'current'
            // })
            //
            // })}, 3000);


        }
    };

    ListController.include(includeDict);
        var RentalListView = ListView.extend({
        config: _.extend({}, ListView.prototype.config, {
            Controller: ListController,
        }),
    });
    viewRegistry.add('product_rental_tree', RentalListView);
});

odoo.define('shopify_app.ProductWidget', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var widget_registry = require('web.widget_registry');

    var LeaveStatsWidget = Widget.extend({
        // template: 'hr_holidays.leave_stats',


        /**
         * @override to fetch data before rendering.
         */
        willStart: function () {
            //
            return Promise.all([this._super(), this._fetchLeaveTypesData()]);
        },
      /**
         * Fetch the number of leaves, grouped by leave type, taken by ``this.employee``
         * in the year of ``this.date``.
         * The resulting data is assigned to ``this.leavesPerType``
         * @private
         * @returns {Promise}
         */
        _fetchLeaveTypesData: function () {

            var self = this;
            var year_date_from = this.date.clone().startOf('year');
            var year_date_to = this.date.clone().endOf('year');

            // return this._rpc({
            //     model: 'hr.leave',
            //     method: 'read_group',
            //     kwargs: {
            //         domain: [['employee_id', '=', this.employee.res_id], ['state', '=', 'validate'], ['date_from', '<=', year_date_to], ['date_to', '>=', year_date_from]],
            //         fields: ['holiday_status_id', 'number_of_days:sum'],
            //         groupby: ['holiday_status_id'],
            //     },
            // }).then(function (data) {
            //     self.leavesPerType = data;
            // });
        }

    });

    widget_registry.add('shopify_product_widget', LeaveStatsWidget);

    return LeaveStatsWidget;
});
