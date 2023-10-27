from odoo import models, fields


class AirportMedicalCompany(models.Model):
    _name = 'airport.medical.company'
    _description = 'Airport medical company model'

    name = fields.Char(string='公司名稱')
    medical_ids = fields.One2many('airport.medical', 'airport_co_id')
