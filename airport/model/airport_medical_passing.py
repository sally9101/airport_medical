from odoo import models, fields


class AirportMedicalPassing(models.Model):
    _name = 'airport.medical.passing'
    _description = 'Airport medical passing model'

    name = fields.Char(string='經過地名稱')
    medical_ids = fields.One2many('airport.medical', 'passing_id')
