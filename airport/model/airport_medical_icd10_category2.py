from odoo import models, fields


class AirportMedicalIcd10Category2(models.Model):
    _name = 'airport.medical.icd10.category2'
    _description = 'Airport medical icd10 category2 model'

    name = fields.Char(string='腫瘤')
    medical_ids = fields.One2many('airport.medical', 'icd10_category2_id')
