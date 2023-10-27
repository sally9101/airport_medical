from odoo import models, fields, api


class AirportMedicalBill(models.Model):
    _name = 'airport.medical.bill'
    _description = 'Airport medical bill model'

    name = fields.Char(string='姓名')
    medical_ids = fields.One2many('airport.medical', 'bill_id')
    Date = fields.Date(default=lambda self: fields.Date.today(), string='日期')
    visitfee = fields.Char(string="初診費")
    ambulancefee = fields.Char(string="救護車費用")
    pleasepay = fields.Boolean(string="請款")
    cash = fields.Boolean(string="現金")
    creditcard = fields.Boolean(string="刷卡")
    payment_status = fields.Selection([
        ('unpaid', '未繳費'),
        ('paid', '已繳費')
    ], string='繳費狀態', default='unpaid')

    total_fee = fields.Float(string="总费用", compute='_compute_total_fee', store=True)

    @api.depends('visitfee', 'ambulancefee')
    def _compute_total_fee(self):
        for record in self:
            total_fee = 0.0
            if record.visitfee:
                total_fee += float(record.visitfee)
            if record.ambulancefee:
                total_fee += float(record.ambulancefee)
            record.total_fee = total_fee
