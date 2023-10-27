from odoo import models, fields


class AirportMedicalIncidentPlace(models.Model):
    _name = 'airport.medical.incident.place'
    _description = 'Airport medical incident place model'

    name = fields.Char(string='事故地點名稱')
    category = fields.Char(string='所屬分類')
    medical_ids = fields.One2many('airport.medical', 'incident_place_id')

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f'{record.category} - {record.name}'))
        return res
