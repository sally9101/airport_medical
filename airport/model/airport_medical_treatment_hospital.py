from odoo import models, fields


class AirportMedicalTreatmentHospital(models.Model):
    _name = 'airport.medical.treatment.hospital'
    _description = 'Airport medical treatment hospital model'

    name = fields.Char(string='在醫院處置的名稱')
    medical_ids = fields.One2many('airport.medical', 'treatment_hospital_id')
