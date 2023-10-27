from odoo import models, fields


class AirportMedicalIcd10Category(models.Model):
    _name = 'airport.medical.icd10.category'
    _description = 'Airport medical icd10 category model'

    name = fields.Char(string='ICD10種類名稱')
    medical_ids = fields.One2many('airport.medical', 'icd10_category_id')
