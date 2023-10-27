from odoo import models, fields


class AirportMedicalIncidentTime(models.Model):
    _name = 'airport.medical.incident.time'
    _description = 'Airport medical incident time model'

    name = fields.Char(string='事發時段')
    medical_ids = fields.One2many('airport.medical', 'incident_time_id')
