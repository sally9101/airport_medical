from odoo import models, fields


class AirportMedicalAttendingPhysician(models.Model):
    _name = 'airport.medical.attending.physician'
    _description = 'Airport medical attending physician model'

    name = fields.Char(string='醫師姓名')
    medical_ids = fields.One2many('airport.medical', 'attending_physician_id')
