from odoo import models, fields


class AirportMedicalIcd10Category6(models.Model):
    _name = 'airport.medical.icd10.category6'
    _description = 'Airport medical icd10 category6 model'

    name = fields.Char(string='神經系統疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category6_id')
