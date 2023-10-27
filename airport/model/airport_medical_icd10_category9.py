from odoo import models, fields


class AirportMedicalIcd10Category9(models.Model):
    _name = 'airport.medical.icd10.category9'
    _description = 'Airport medical icd10 category9 model'

    name = fields.Char(string='呼吸系統疾病名稱')
    medical_ids = fields.One2many('airport.medical', 'icd10_category9_id')
