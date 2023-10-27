from odoo import models, fields


class AirportMedicalCome(models.Model):
    _name = 'airport.medical.come'
    _description = 'Airport medical come reason model'

    name = fields.Char(string='原因名稱')
    medical_ids = fields.One2many('airport.medical', 'come_reason_id')
