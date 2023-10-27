from odoo import models, fields


class AirportMedicalIcd10Category12(models.Model):
    _name = 'airport.medical.icd10.category12'
    _description = 'Airport medical icd10 category12 model'

    name = fields.Char(string='肌肉骨骼系統和結締組織疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category12_id')
