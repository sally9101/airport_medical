from odoo import models, fields


class AirportMedicalChiefComplaint(models.Model):
    _name = 'airport.medical.chief.complaint'
    _description = 'Airport medical chief complaint'

    name = fields.Char(string='主訴名稱')
    medical_ids = fields.One2many('airport.medical', 'chief_complaint_id')
