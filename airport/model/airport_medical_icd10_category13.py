from odoo import models, fields


class AirportMedicalIcd10Category13(models.Model):
    _name = 'airport.medical.icd10.category13'
    _description = 'Airport medical icd10 category13 model'

    name = fields.Char(string='泌尿生殖系統疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category13_id')
