from odoo import models, fields


class AirportMedicalComment(models.Model):
    _name = 'airport.medical.comment'
    _description = 'Airport medical comment model'

    name = fields.Char(string='醫師囑言名稱')
    medical_ids = fields.One2many('airport.medical', 'comment_id')
