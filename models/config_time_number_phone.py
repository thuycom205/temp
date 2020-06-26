from odoo import models, fields, api


class ConfigTimeNumberPhong(models.Model):
    _name = 'config.time.phone.number'

    status = fields.Char()
    # Monday
    start_monday = fields.Char(default='0000')
    end_monday = fields.Char(default='2359')
    # Tuesday
    start_tuesday = fields.Char(default='0000')
    end_tuesday = fields.Char(default='2359')
    # Wednesday
    start_wednesday = fields.Char(default='0000')
    end_wednesday = fields.Char(default='2359')
    # Thursday
    start_thursday = fields.Char(default='0000')
    end_thursday = fields.Char(default='2359')
    # Friday
    start_friday = fields.Char(default='0000')
    end_friday = fields.Char(default='2359')
    # Saturday
    start_saturday = fields.Char(default='0000')
    end_saturday = fields.Char(default='2359')
    # Sunday
    start_sunday = fields.Char(default='0000')
    end_sunday = fields.Char(default='2359')

    # setup_time = fields.Boolean(default=False)
    @api.model
    def create(self, vals):
        res = super(ConfigTimeNumberPhong, self).create(vals)
        current_id = self.env['res.users'].search([('id', '=', self.env.uid)])
        val = {
            'config_time_hours': res.id
        }
        current_id.update(val)
        return res

