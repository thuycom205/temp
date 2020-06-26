odoo.define('rental.RentalOrderListController', function (require) {
"use strict";
var pyUtils = require('web.py_utils');
var Domain = require('web.Domain');
var session = require('web.session');

var core = require('web.core');
var _t = core._t;

var ListController = require('web.ListController');
var dropdownMenu = require('web.DropdownMenu');
    // var SearchFilterMenu = require('web.FiltersMenu');

var ControlPanelController = require('web.ControlPanelController');
var ControlPanelModel = require('web.ControlPanelModel');
//
    ControlPanelModel.include({
    _getDomain: function () {
        var self = this;
        var domains = this.query.map(function (groupId) {
            var group = self.groups[groupId];
            return self._getGroupDomain(group);
        });
       var  x = pyUtils.assembleDomains(domains, 'AND');
       if (x.indexOf('is_rental_order') !== -1 && window.rental_filter_keyword)
           x ='["&", ("is_rental_order", "=", True), "|", "|", ["name", "ilike", ' + window.rental_filter_keyword  + '], ["client_order_ref", "ilike", ' + window.rental_filter_keyword  + ' ], ["partner_id", "child_of",' + window.rental_filter_keyword  + ']]';
       return x;
    },
});
// web.ControlPanelModel
ControlPanelController.include({

    init: function (parent, model, renderer, params) {
        this._super.apply(this, arguments);

        this.modelName = params.modelName;
        core.bus.on('react_search', this, this._onReactSearch);

    },
      /**
     * @private
     * @returns {Promise}
     */
    _reportNewQueryAndRender: function () {
        this.trigger_up('search', this.model.getQuery());
                  console.log('query ====?');

        console.log(this.model.getQuery());
        var state = this.model.get();
          console.log(state);

        return this.renderer.updateState(state);
    },
     _onReactSearch: function(code) {
                   this.trigger_up('autocompletion_filter', {
                filterId: '__filter__7',
                autoCompleteValues: {label: '039' , value: '039'},
            });

    }
});

dropdownMenu.include({
    init: function () {
        this._super.apply(this, arguments);
        console.log(this.template);
        if (this.template == 'web.DropdownMenu' && window.menuItem == undefined)  {
                window.menuItem = this.items;
                window.dropdownMenu = this;
                    this._onRentalOrderFilter = function (id) {
                    this.trigger_up('menu_item_clicked', {id: '__filter__24'});
                      console.log('filter menu from react');

                      console.log(id);
                }
              core.bus.on('menu_item_clicked', this, this._onRentalOrderFilter);

        }
    },
});

var x1 = require('web.ControlPanelRenderer')

var qweb = core.qweb;


var RentalOrderListController = ListController.extend({

    // -------------------------------------------------------------------------
    // Public
    // -------------------------------------------------------------------------

    init: function (parent, model, renderer, params) {
        this.context = renderer.state.getContext();
        return this._super.apply(this, arguments);
    },

    _onRentalOrderFilter: function(id) {
        window.dropdownMenu.trigger_up('menu_item_clicked', {id: '__filter__24'});

        console.log(id);

    },

        _getSearchDomain: function () {
        var searchDomain = this._super.apply(this, arguments) || [];
        return searchDomain.concat([['name', 'ilike', '039']]);
    },
    /**
     * @override
     */
    renderButtons: function ($node) {
        var rootDiv=document.createElement('div');
        rootDiv.setAttribute("id", "root");
        document.getElementsByTagName('body')[0].appendChild(rootDiv);
        window.coreobj = core;

        // var client_action = window.coreobj.action_registry.get('client_action');
        //
        // console.log('trong ');
        // console.log(window.coreobj.action_registry.keys);


        var script = document.createElement('script');

        script.type='text/javascript';

        script.src = "/shopify_app/static/src/js/bundle.js";

        document.getElementsByTagName('body')[0].appendChild(script);

        console.log(x1.$subMenus);
        // core.bus.on('menu_item_clicked', this, this._onRentalOrderFilter);
        // if (this.context.params!= null && this.context.params!= undefined && this.context.params.view_type == 'list') {
        //       setInterval(function(){
        //      jQuery('.o_controller_with_searchpanel').css('display' , 'none');
        //      jQuery('.o_control_panel').css('display' , 'none');
        //      jQuery('.o_main_navbar').css('display' , 'none');
        //      }, 1000);
        // }





            //  <div id="root"></div>
            // <script type="text/javascript" src="/mrp_mps/static/src/js/bundle.js"/>
        this._super.apply(this, arguments);
        // if (this.context.no_at_date) {
        //     return;
        // }
        // var $buttonToDate = $(qweb.render('InventoryReport.Buttons'));
        // $buttonToDate.on('click', this._onOpenWizard.bind(this));
        //
        // $buttonToDate.prependTo($node.find('.o_list_buttons'));
    },

    // -------------------------------------------------------------------------
    // Handlers
    // -------------------------------------------------------------------------

    /**
     * Handler called when the user clicked on the 'Inventory at Date' button.
     * Opens wizard to display, at choice, the products inventory or a computed
     * inventory at a given date.
     */
    _onOpenWizard: function () {
        var state = this.model.get(this.handle, {raw: true});
        var stateContext = state.getContext();
        var context = {
            active_model: this.modelName,
        };
        if (stateContext.default_product_id) {
            context.product_id = stateContext.default_product_id;
        } else if (stateContext.product_tmpl_id) {
            context.product_tmpl_id = stateContext.product_tmpl_id;
        }
        this.do_action({
            res_model: 'stock.quantity.history',
            views: [[false, 'form']],
            target: 'new',
            type: 'ir.actions.act_window',
            context: context,
        });
    },
});

return RentalOrderListController;

});
