from odoo import models, fields


class AirportMedicalRace(models.Model):
    _name = 'airport.medical.race'
    _description = 'Airport medical race model'

    name = fields.Char(string='種族名稱')
    medical_ids = fields.One2many('airport.medical', 'race_id')
