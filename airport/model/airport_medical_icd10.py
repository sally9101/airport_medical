from odoo import models, fields


class AirportMedicalInitialDiagnosisIcd10(models.Model):
    _name = 'airport.medical.icd10'
    _description = 'Airport medical initial diagnosis icd10'

    name = fields.Char(string='初步診斷ICD')
    medical_ids = fields.One2many('airport.medical', 'initial_diagnosis_icd10')
