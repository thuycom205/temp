from odoo import models, fields


class ConfigBasicWhatsApp(models.Model):
    _name = 'config.basic.whats.app'

    # Button Text & Design
    config_phone_number = fields.One2many('config.phone.number', 'config_basic_id')
    select_colour = fields.Selection([('single', 'Single colour'),
                                      ('gradient', 'Gradient of two colours')])
    single_colour = fields.Boolean(string='Single colour')
    gradient_colours = fields.Boolean(string='Grandient of two colours')
    background_colour_1 = fields.Char(string='Background colour 1')
    background_colour_2 = fields.Char(string='Background colour 2')
    icon_colour = fields.Char(string='Icon colour')
    button_color = fields.Char(string='Button text colour')
    chat_button_text = fields.Char(string='Chat Button Text')
    whatsapp_message_body = fields.Text(string='WhatsApp Message Body')
    include_url = fields.Boolean()

    # Callout Car
    show_callout_button = fields.Boolean()
    callout_car_text = fields.Char(string='')
    callout_card_delay = fields.Integer(string='Callout card delay')

    # Greetings Widget
    select_colour_widget = fields.Selection([('single', 'Single colour'),
                                             ('gradient', 'Gradient of two colours')])
    single_colour_widget = fields.Boolean(string='Single colour')
    gradient_colours_widget = fields.Boolean(string='Grandient of two colours')
    background_colour_1_widget = fields.Char(string='Background colour 1')
    background_colour_2_widget = fields.Char(string='Background colour 2')
    title_widget = fields.Char(string='Title')
    help_text = fields.Char(string='Help Text')
    randomise_order = fields.Boolean(string='Randomise order')

    # Button Display & Position

    chat_button_display = fields.Selection([('mobile_desktop', 'Mobile + Desktop'),
                                            ('mobile_only', 'Mobile only'),
                                            ('desktop_only', 'Desktop only')])

    button_mobile_position = fields.Selection([('mobile_left', 'Left'),
                                               ('mobile_right', 'Right')])

    button_desktop_position = fields.Selection([('desktop_left', 'Left'),
                                                ('desktop_right', 'Right')])

    height_mobile = fields.Integer(string='Height Mobile')
    height_desktop = fields.Integer(string='Height Desktop')

    edge_mobile = fields.Integer(string='EDGE mobile')
    edge_desktop = fields.Integer(string='EDGE desktop')

    set_height_button_page = fields.Boolean()
    height_mobile_page = fields.Integer(string='Height Mobile Page')
    height_desktop_page = fields.Integer(string='Height Desktop Height')

    # Pages to display
    home_page = fields.Boolean(default=False)
    collections = fields.Boolean(default=False)
    product_page = fields.Boolean(default=False)
    cart = fields.Boolean(default=False)
    thank_page = fields.Boolean(default=False)
    blog_post = fields.Boolean(default=False)
    url_ending = fields.Boolean(default=False)
    account_page = fields.Boolean(default=False)

    # Advanced setting
    event_category = fields.Char(string='Event Category')
    event_lable = fields.Char(string='Event Label')
    event_action = fields.Char(string='Event Action')
    event_name = fields.Char(string='Event Name')

    def action_open_cart(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'button_template_client_action',
            'target': 'new',
        }
