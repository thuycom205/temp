odoo.define('whatsapp.AbstractController', function (require) {
"use strict";

var ActionMixin = require('web.ActionMixin');
var ajax = require('web.ajax');
var concurrency = require('web.concurrency');
var config = require('web.config');
var core = require('web.core');
var mvc = require('web.mvc');

var session = require('web.session');

var QWeb = core.qweb;
var AbstractController = require('web.AbstractController');

// web.ControlPanelModel
AbstractController.include({

    start: function () {
        var xcheck ='<span> Order status</span><fieldset class="_1XaJd _2DG-w" id="financial_status[]" aria-invalid="false"><ul class="_3J4nR"><li><label class="_2EHn3" for="PolarisCheckbox18"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox18" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="authorized"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Authorized</span></label></li><li><label class="_2EHn3" for="PolarisCheckbox19"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox19" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="paid"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Paid</span></label></li><li><label class="_2EHn3" for="PolarisCheckbox20"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox20" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="partially_refunded"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Partially refunded</span></label></li><li><label class="_2EHn3" for="PolarisCheckbox21"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox21" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="partially_paid"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Partially paid</span></label></li><li><label class="_2EHn3" for="PolarisCheckbox22"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox22" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="pending"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Pending</span></label></li><li><label class="_2EHn3" for="PolarisCheckbox23"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox23" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="refunded"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Refunded</span></label></li><li><label class="_2EHn3" for="PolarisCheckbox24"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox24" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="unpaid"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Unpaid</span></label></li><li><label class="_2EHn3" for="PolarisCheckbox25"><span class="_2QQVi"><span class="idoor"><input id="PolarisCheckbox25" name="financial_status[]" type="checkbox" class="_1Kfuo" aria-invalid="false" role="checkbox" aria-checked="false" value="voided"><span class="_3glI3"></span><span class="_3aRjU"><span class="_2-hnq"><svg viewBox="0 0 20 20" class="v3ASA" focusable="false" aria-hidden="true"><path d="M8.315 13.859l-3.182-3.417a.506.506 0 0 1 0-.684l.643-.683a.437.437 0 0 1 .642 0l2.22 2.393 4.942-5.327a.437.437 0 0 1 .643 0l.643.684a.504.504 0 0 1 0 .683l-5.91 6.35a.437.437 0 0 1-.642 0"></path></svg></span></span></span></span><span class="_3tI7Z">Voided</span></label></li></ul></fieldset>';
        var orderStatus  = ' <span> Status</span><select> <option value="open"> open</option> <option> paid</option></select>'
        var self = this;
        if (this._searchPanel) {
            window.myContent = this.$('.o_content');
            if (window.mySearchBar != undefined) window.mySearchBar.prependTo(this.$('.o_content'));
            this.$('.o_content')
                .addClass('o_controller_with_searchpanel')
                .prepend(this._searchPanel.$el);
        }

        this.$el.addClass('o_view_controller');

        return this._super.apply(this, arguments).then(function () {
            var prom;
            if (self._controlPanel) {
                // render the ControlPanel elements (buttons, pager, sidebar...)
                prom = self._renderControlPanelElements().then(function (elements) {
                    self.controlPanelElements = elements;
                    self._controlPanel.$el.prependTo(self.$el);
                });
            }
            return Promise.resolve(prom);
        }).then(function () {
            return self._update(self.initialState);
        });
    },
});

});
