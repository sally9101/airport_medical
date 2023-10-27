from odoo import models, fields


class AirportMedicalDeparture(models.Model):
    _name = 'airport.medical.departure'
    _description = 'Airport medical departure model'

    name = fields.Char(string='啟程地名稱')
    medical_ids = fields.One2many('airport.medical', 'departure_id')
