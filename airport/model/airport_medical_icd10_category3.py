from odoo import models, fields


class AirportMedicalIcd10Category3(models.Model):
    _name = 'airport.medical.icd10.category3'
    _description = 'Airport medical icd10 category3 model'

    name = fields.Char(string='血液及造血器官疾病和某些涉及免疫系統的疾患')
    medical_ids = fields.One2many('airport.medical', 'icd10_category3_id')
