# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime
import logging
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class fleet_extension_model(models.Model):
    _inherit = 'fleet.vehicle'

    leasing_company = fields.Many2one('res.partner', string="Leasing company")
    leasing_date = fields.Date(string='Lease expiration date')
    # insurance_company = fields.Many2one(string='Insurance company', related='log.contract.insurer_id')
    # insurance_date = fields.Date(string='End date of insurance', related='log.contract.expiration_date')
    insurance_number = fields.Char(string='Insurance policy number')
    wheel_size = fields.Char(string='Wheel size')
    fire_extinguisher_date = fields.Date(string='Expiration date of fire extinguisher')
    technical_review = fields.Date(string='Date of technical inspection')
    spare_wheel = fields.Boolean(string='Spare wheel')
    pin_card = fields.Integer(string='Card PIN')
    pressure_sensor = fields.Boolean(string='Pressure sensor')
    vignette = fields.Char(string='Vignette')
    vignette_date = fields.Date(string='Expiration date of the vignette')


