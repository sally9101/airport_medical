from odoo import models, fields


class AirportMedicalArrival(models.Model):
    _name = 'airport.medical.arrival'
    _description = 'Airport medical arrival model'

    name = fields.Char(string='目的地名稱')
    medical_ids = fields.One2many('airport.medical', 'arrival_id')
    
