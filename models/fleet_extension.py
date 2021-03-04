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
    fire_extinguisher_date = fields.Date(string='Expiration date of fire extinguisher', help='Does it exist in the car.')
    technical_review = fields.Date(string='Date of technical inspection')
    spare_wheel = fields.Boolean(string='Spare wheel', help='Does it exist in the car.')
    pin_card = fields.Integer(string='Card PIN', help="This is the pin code for the company's fleet card.")
    pressure_sensor = fields.Boolean(string='Pressure sensor', help='Does it exist in the car.')
    vignette = fields.Char(string='Vignette')
    vignette_date = fields.Date(string='Expiration date of the vignette')

    def set_insurance_info(self):
        for rec in self:
            if not self.env['fleet.service.type'].search([('category', '=', 'contract'), ('name', '=', 'Insurance')]):
                self.env['fleet.service.type'].create({
                    'name': 'Insurance',
                    'category': 'contract'
                })

            if not self.env['fleet.service.type'].search([('category', '=', 'contract'), ('name', '=', 'Leasing')]):
                self.env['fleet.service.type'].create({
                    'name': 'Leasing',
                    'category': 'contract'
                })

            if not self.env['fleet.service.type'].search([('category', '=', 'contract'), ('name', '=', 'PKN Orlen')]):
                self.env['fleet.service.type'].create({
                    'name': 'PKN Orlen',
                    'category': 'contract'
                })

            veh_ins_log = self.env['fleet.vehicle.log.contract'].search([('active', '=', True), ('cost_subtype_id', '=', 'Insurance'), ('state', '=', 'open'), ('vehicle_id', '=', rec.name)])

            if len(veh_ins_log) == 1:
                rec.insurance_date = veh_ins_log['expiration_date']
                rec.insurance_company = veh_ins_log['insurer_id']['name']
