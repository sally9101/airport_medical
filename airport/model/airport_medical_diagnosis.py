from odoo import models, fields


class AirportMedicalDiagnosis(models.Model):
    _name = 'airport.medical.diagnosis'
    _description = 'Airport medical diagnosis'

    icd10_cm = fields.Char(string='ICD-10編碼')
    use = fields.Integer(string='是否使用')
    name_en = fields.Char(string='英文名稱')
    name_ch = fields.Char(string='中文名稱')
    medical_ids = fields.One2many('airport.medical', 'diagnosis_id')

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, f'{record.name_en} - {record.name_ch}'))
        return res
