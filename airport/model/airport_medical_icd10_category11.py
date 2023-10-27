from odoo import models, fields


class AirportMedicalIcd10Category11(models.Model):
    _name = 'airport.medical.icd10.category11'
    _description = 'Airport medical icd10 category11 model'

    name = fields.Char(string='皮膚和皮下組織疾病')
    medical_ids = fields.One2many('airport.medical', 'icd10_category11_id')
