from odoo import models, fields


class AirportMedicalIcd10Category4(models.Model):
    _name = 'airport.medical.icd10.category4'
    _description = 'Airport medical icd10 category4 model'

    name = fields.Char(string='內分泌，營養和代謝疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category4_id')
