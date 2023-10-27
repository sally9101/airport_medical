from odoo import models, fields


class AirportMedicalAttendingNurse(models.Model):
    _name = 'airport.medical.attending.nurse'
    _description = 'Airport medical attending nurse'

    name = fields.Char(string='護士姓名')
    medical_ids = fields.One2many('airport.medical', 'attending_nurse_id')
