# -*- coding: utf-8 -*-

from odoo import fields, models
import logging

_logger = logging.getLogger(__name__)


class fleet_extension_model(models.Model):
    _inherit = 'fleet.vehicle'

    leasing_company = fields.Many2one('res.partner', string="Leasing company")
    leasing_date = fields.Date(string='Leasing expiration date')
    insurance_company = fields.Char(string='Insurance company', compute='set_insurance_info', readonly=True)
    insurance_date = fields.Date(string='End date of insurance', compute='set_insurance_info', readonly=True)
    insurance_number = fields.Char(string='Insurance policy number')
    wheel_size = fields.Char(string='Wheel size')
    fire_extinguisher_date = fields.Date(string='Expiration date of fire extinguisher')
    technical_review = fields.Date(string='Date of technical inspection')
    spare_wheel = fields.Boolean(string='Spare wheel')
    pin_card = fields.Integer(string='Card PIN')
    pressure_sensor = fields.Boolean(string='Pressure sensor')
    vignette = fields.Char(string='Vignette')
    vignette_date = fields.Date(string='Expiration date of the vignette')

    def set_insurance_info(self):
        for rec in self:
            veh_log = self.env['fleet.vehicle.log.contract'].search([('active', '=', True), ('state', '=', 'open'), ('vehicle_id', '=', rec.name)])

            if len(veh_log) == 1:
                rec.insurance_date = veh_log['expiration_date']
                rec.insurance_company = veh_log['insurer_id']['name']
