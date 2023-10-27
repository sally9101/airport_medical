from odoo import models, fields


class AirportMedicalResult(models.Model):
    _name = 'airport.medical.result'
    _description = 'Airport medical result model'

    name = fields.Char(string='結果名稱')
    medical_ids = fields.One2many('airport.medical', 'result_id')
