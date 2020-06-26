odoo.define('whatsapp.client_action_button', function (require) {
'use strict';

var concurrency = require('web.concurrency');
var core = require('web.core');
var AbstractAction = require('web.AbstractAction');
var Dialog = require('web.Dialog');
var field_utils = require('web.field_utils');
var session = require('web.session');

var QWeb = core.qweb;
var _t = core._t;
window.core = core;


var ClientAction = AbstractAction.extend({
    contentTemplate: 'ButtonTemplate',
    hasControlPanel: false,
    withSearchBar: false,
    loadControlPanel: false,
    phone_numbers:[],
    button_text_color:[],
    config_time_ids:[],
    callout:[],
    button_position:[],
    pages_display:[],
        events: {
        'change .o_mrp_mps_input_forcast_qty': '_onChangeForecast',
        'change .o_mrp_mps_input_replenish_qty': '_onChangeToReplenish',
        'click .o_basic_setting_add_number': '_onClickAddNumber',
        'click .o_basic_setting_time_number': '_onClickSettingTime',
        'click .o_save_edit_button_color_1': '_onClickEditColorButton',
        'click .o_save_edit_callout_card': '_onClickEditCalloutCard',
        'click .o_save_edit_button_display_position': '_onClickEditButtonDisplayPosition',
         'click .o_save_edit_pages_to_display': '_onClickEditPagesToDisPlay',
    },

    _onClickAddNumber: function () {
   console.log('click add button');
        var context = {
        'mode': 'customers',
        'default_country_code': '84',
        };
        this.do_action({
        type: 'ir.actions.act_window',
        res_model: 'config.phone.number',
        views: [[false, 'form']],
        target: 'new',
        context: context,
        });
},
        willStart: function () {
        var self = this;
        var _super = this._super.bind(this);
        var args = arguments;
        var user = session.uid
        window.core.bus.on('shooted', this, this.whatsapp_edit_number);
        window.core.bus.on('edit_time',this,this.whatsapp_edit_time);
        window.core.bus.on('ColorButton',this,this.whatsapp_edit_color);
        window.core.bus.on('CalloutButton',this,this.whatsapp_edit_callout);
        window.core.bus.on('ButtonPosition',this,this.whatsapp_edit_button_position);
        window.core.bus.on('PagesButton',this,this.whatsapp_edit_button_pages);
        // Form Basic setting Number
        var def_control_panel = this._rpc({
            model: 'config.phone.number',
            method: 'search_read',
            args:[[["create_uid","=",user]],["id",'country_code','phone_number']],
            kwargs: {context: session.user_context},
        })
        .then(function (result) {
            console.log(result);
            self.phone_numbers = result;
            self.renderElement();
        });

        // Form Edit hours
        var def_config_time = this._rpc({
            model:'res.users',
            method: 'search_read',
            args :[[["id","=",user]]]
        }).then(function(result){
           console.log(result)
           self.config_time_ids = result;
           self.renderElement();

        });

        var def_config_button_color = this._rpc({
            model:'config.button.text.design',
            method: 'search_read',
            args :[[["user_id","=",user]]]
        }).then(function(result){
            console.log(result)
            self.button_text_color = result;

            self.renderElement();
        })

        var def_config_callout = this._rpc({
            model:'config.callout.card',
            method: 'search_read',
            args :[[["user_id","=",user]]]
        }).then(function(result){
            console.log(result)
            self.callout = result;

            self.renderElement();
        })

        var def_config_button_position = this._rpc({
            model:'config.button.display.position',
            method: 'search_read',
            args :[[["user_id","=",user]]]
        }).then(function(result){
            console.log(result)
            self.button_position = result;

            self.renderElement();
        })


        var def_config_pages_display = this._rpc({
            model:'config.page.to.display',
            method: 'search_read',
            args :[[["user_id","=",user]]]
        }).then(function(result){
            console.log(result)
            self.pages_display = result;

            self.renderElement();
        })
          return _super.apply(self, args);

    },
    whatsapp_edit_number(element) {
        console.log('Bus success')
        var eId = jQuery(element).attr('id');
        console.log(element);
        this.phone_numbers.push({id: 10, phone_number: 8888});
        var context = {
            'mode': 'customers',
            'default_country_code': '84',
        };
        this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'config.phone.number',
            res_id: parseInt(element),
            views: [[false, 'form']],
            target: 'new',
            context: context,
        });

        // jQuery('.whatsapp-numbers-table').html('<div>By Reach</div>');
    },
    whatsapp_edit_time(element){
      this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'config.time.phone.number',
            res_id: parseInt(element),
            views: [[false, 'form']],
            target: 'new',
      })
    },
    whatsapp_edit_color(element){
      this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'config.button.text.design',
            res_id: parseInt(element),
            views: [[false, 'form']],
            target: 'new',
      })
    },
    whatsapp_edit_callout(element){
              this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'config.callout.card',
            res_id: parseInt(element),
            views: [[false, 'form']],
            target: 'new',
      })
    },
    whatsapp_edit_button_position(element){
            this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'config.button.display.position',
            res_id: parseInt(element),
            views: [[false, 'form']],
            target: 'new',
      })
    },
    whatsapp_edit_button_pages(element){
         this.do_action({
            type: 'ir.actions.act_window',
            res_model: 'config.page.to.display',
            res_id: parseInt(element),
            views: [[false, 'form']],
            target: 'new',
    })},
    _onClickSettingTime:function(){
        console.log('ConfigTime')
        this.do_action({
            type :'ir.actions.act_window',
            res_model: 'config.time.phone.number',
            views :[[false,'form']],
            target :'new',
        })
    },
    _onClickEditColorButton:function(){
        console.log('Color Edit')
        this.do_action({
             type :'ir.actions.act_window',
            res_model: 'config.button.text.design',
            views :[[false,'form']],
            target :'new',
        });
    },
    _onClickEditCalloutCard:function(){
        this.do_action({
             type :'ir.actions.act_window',
            res_model: 'config.callout.card',
            views :[[false,'form']],
            target :'new',
        });
    },
    _onClickEditButtonDisplayPosition:function(){
        this.do_action({
            type :'ir.actions.act_window',
            res_model: 'config.button.display.position',
            views :[[false,'form']],
            target :'new',
        });
    },
    _onClickEditPagesToDisPlay:function(){
        this.do_action({
            type :'ir.actions.act_window',
            res_model: 'config.page.to.display',
            views :[[false,'form']],
            target :'new',
        });
    }

});
window.whatsapp_edit_number = function(element) {
    var eId = jQuery(element).attr('id');
    console.log(eId);
}
core.action_registry.add('button_template_client_action', ClientAction);

return ClientAction;

});
