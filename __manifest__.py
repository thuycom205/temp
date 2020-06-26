# -*- coding: utf-8 -*-
{
    'name': "shopify_app",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Magenest",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale','base_setup', 'product', 'analytic', 'sale_renting'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/groups/security_groups.xml',
        'views/views.xml',
        'views/shopify_app.xml',
        'views/res_config_settings_views.xml',
        'views/config_cart_views.xml',
        'views/message_logs_views.xml',
        'views/config_order_crm.xml',
        'views/config_sms_whats_app_notif.xml',
        'views/config_manual_orders_crm.xml',
        'views/config_manual_abandoned_cart_view.xml',
        'views/config_basic_whatsapp_view.xml',
        'views/config_phone_number_view.xml',
        'views/config_time_number_phone_views.xml',
        'views/config_cash_on_delivery.xml',
        'views/message_manual_abandoned_1.xml',
        'views/message_manual_abandoned_2.xml',
        'views/message_order_crm_ask_review.xml',
        'views/message_order_crm_cod_confirm.xml',
        'views/message_order_crm_confirm.xml',
        'views/message_order_crm_new_product.xml',
        'views/message_order_crm_repeat_customer.xml',
        'views/message_order_crm_tracking.xml',
        'views/message_order_first_purchase.xml',
        'views/message_template.xml',
        'views/list_order_crm.xml',
        'views/list_abandoned_cart.xml',
        'views/config_button_text_design.xml',
        'views/config_callout_card.xml',
        'views/config_button_display_position.xml',
        'views/config_pages_to_display.xml',


    ],
    'qweb': [
            "static/src/xml/rental_product_wizard_views.xml",
            "static/src/xml/qweb_button_template.xml",
            "static/qweb_config_basic.xml",
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'css': ['static/src/css/shopify_billing.css'],

    'application': True

}
