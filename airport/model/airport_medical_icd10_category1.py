from odoo import models, fields


class AirportMedicalIcd10Category1(models.Model):
    _name = 'airport.medical.icd10.category1'
    _description = 'Airport medical icd10 category1 model'

    name = fields.Char(string='某些傳染病和寄生蟲病疾病名稱')
    medical_ids = fields.One2many('airport.medical', 'icd10_category1_id')
