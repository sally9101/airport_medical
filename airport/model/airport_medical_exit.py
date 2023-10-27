from odoo import models, fields


class AirportMedicalExit(models.Model):
    _name = 'airport.medical.exit'
    _description = 'Airport medical exit model'

    name = fields.Char(string='出入境')
    medical_ids = fields.One2many('airport.medical', 'exit_id')
