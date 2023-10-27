from odoo import models, fields


class AirportMedicalTreatment(models.Model):
    _name = 'airport.medical.treatment'
    _description = 'Airport medical treatment model'

    name = fields.Char(string='處置名稱')
    category = fields.Char(string='類別')
    value = fields.Integer(string='Value')
    medical_ids = fields.One2many('airport.medical', 'treatment_id')

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f'{record.category} - {record.name}'))
        return res
