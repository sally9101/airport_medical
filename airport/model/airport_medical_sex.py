from odoo import models, fields


class AirportMedicalSex(models.Model):
    _name = 'airport.medical.sex'
    _description = 'Airport medical sex model'

    name = fields.Char(string='性別名稱')
    medical_ids = fields.One2many('airport.medical', 'sex_id')
