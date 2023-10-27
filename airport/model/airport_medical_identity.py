from odoo import models, fields


class AirportMedicalIdentity(models.Model):
    _name = 'airport.medical.identity'
    _description = 'Airport medical identity model'

    name = fields.Char(string='身分名稱')
    medical_ids = fields.One2many('airport.medical', 'identity_id')
