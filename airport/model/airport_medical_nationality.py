from odoo import models, fields


class AirportMedicalNationality(models.Model):
    _name = 'airport.medical.nationality'
    _description = 'Airport medical nationality model'

    name = fields.Char(string='國家名稱')
    medical_ids = fields.One2many('airport.medical', 'nationality_id')
