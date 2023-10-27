from odoo import models, fields


class AirportMedicalIcd10Category8(models.Model):
    _name = 'airport.medical.icd10.category8'
    _description = 'Airport medical icd10 category8 model'

    name = fields.Char(string='循環系統疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category8_id')
