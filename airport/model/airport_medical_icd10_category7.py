from odoo import models, fields


class AirportMedicalIcd10Category7(models.Model):
    _name = 'airport.medical.icd10.category7'
    _description = 'Airport medical icd10 category7 model'

    name = fields.Char(string='耳和乳突疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category7_id')
