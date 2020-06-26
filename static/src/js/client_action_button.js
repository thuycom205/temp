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

var ClientAction = AbstractAction.extend({
    contentTemplate: 'ButtonTemplate',
});

core.action_registry.add('whatsapp.client_action_button', ClientAction);

return ClientAction;

});

odoo.define('whatsapp.client_action_button', function (require) {
'use strict';

var concurrency = require('web.concurrency');
var core = require('web.core');
var Widget = require('web.AbstractAction');
var Dialog = require('web.Dialog');
var field_utils = require('web.field_utils');
var session = require('web.session');

var QWeb = core.qweb;
var _t = core._t;

var ButtonAction = Widget.extend({
           events: {
            'click .button_style_template': 'onclick_button_style',
        },
    onclick_button_style: function () {
        this.do_action({
            type: 'ir.actions.client',
            tag: 'button_template_client_action',
            views: [[false, 'form']],
            target: 'current',
        });
        },
});
return ButtonAction;
});