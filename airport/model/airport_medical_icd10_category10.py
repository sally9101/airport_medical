from odoo import models, fields


class AirportMedicalIcd10Category10(models.Model):
    _name = 'airport.medical.icd10.category10'
    _description = 'Airport medical icd10 category10 model'

    name = fields.Char(string='消化系統疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category10_id')
