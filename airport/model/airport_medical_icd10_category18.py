from odoo import models, fields


class AirportMedicalIcd10Category18(models.Model):
    _name = 'airport.medical.icd10.category18'
    _description = 'Airport medical icd10 category18 model'

    name = fields.Char(string='損傷、中毒和外因的某些其他後果')
    medical_ids = fields.One2many('airport.medical', 'icd10_category18_id')
