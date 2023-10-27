from odoo import models, fields


class AirportMedicalIcd10Category5(models.Model):
    _name = 'airport.medical.icd10.category5'
    _description = 'Airport medical icd10 category5 model'

    name = fields.Char(string='精神和行為疾患名稱')
    medical_ids = fields.One2many('airport.medical', 'icd10_category5_id')
