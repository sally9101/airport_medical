from odoo import models, fields, api
from odoo.exceptions import ValidationError
import datetime
import logging

class AirportMedical(models.Model):
    _name = 'airport.medical'
    _description = 'Airport medical visit model'

    name = fields.Char(string='姓名')
    birthday = fields.Date(string='生日')
    sex_id = fields.Many2one('airport.medical.sex', string='性別')
    come_reason_id = fields.Many2one('airport.medical.come', string='為何至機場')
    nationality_id = fields.Many2one('airport.medical.nationality', string='國籍')
    race_id = fields.Many2one('airport.medical.race', string='種族')
    airport_co_id = fields.Many2one('airport.medical.company', string='航空公司')
    departure_id = fields.Many2one('airport.medical.departure', string='啟程地')
    passing_id = fields.Many2one('airport.medical.passing', string='經過地')
    arrival_id = fields.Many2one('airport.medical.arrival', string='目的地')
    patient_name =fields.Char(string='病患姓名')
    nationality_id = fields.Many2one('airport.medical.nationality', string='國籍')
    sex_id = fields.Many2one('airport.medical.sex', string='性別')
    birthday = fields.Date(default=lambda self: fields.Date.today(), string='生日')
    airport_co_id = fields.Many2one('airport.medical.company', string='航空公司')
    flight_number = fields.Char(string='班機')
    incident_date = fields.Date(default=lambda self: fields.Date.today(), string='事發日期')
    incident_place_id = fields.Many2one('airport.medical.incident.place', string='事故地點')
    notify_staff = fields.Char(string='通報人員')
    immigration_status1 = fields.Boolean(string='出境')
    immigration_status2 = fields.Boolean(string='入境')
    immigration_status3 = fields.Boolean(string='過境')
    initial_diagnosis = fields.Text(string='初步診斷')
    initial_diagnosis_icd10 =fields.Many2one('airport.medical.icd10.category')
    follow_up_results = fields.Selection(string='後續結果',selection=[('自行返家', '自行返家'), ('繼續搭機', '繼續搭機'), ('轉送至', '轉送至:'), ('醫療中心觀察', '醫療中心觀察'), ('空跑', '空跑'), ('其他', '其他')],
        help="Type is used to separate Leads and Opportunities")
    follow_up_results_replenish = fields.Char(string=' ')
    medical_bills = fields.Char(string='醫療費用收費', readonly=True)
    medical_bills_yes = fields.Boolean(string='是')
    medical_bills_no = fields.Boolean(string='否')
    charge_amount = fields.Char(string='收費金額')
    T1_telephone_number_of_Operation_Safety_Department = fields.Boolean(string='T1-032733578')
    T2_telephone_number_of_Operation_Safety_Department = fields.Boolean(string='T2-032733367')
    Medical_Center_T1_Telephone = fields.Boolean(string='T1-033834225')
    Medical_Center_T2_Telephone = fields.Boolean(string='T2-033983485')
    incident_time_id = fields.Many2one('airport.medical.incident.time', string='事發時段')
    chief_complaint_id = fields.Many2one('airport.medical.chief.complaint', string='主訴')
    diagnosis_id = fields.Many2one('airport.medical.diagnosis', string='診斷')
    diagnosis_1 = fields.Many2one('airport.medical.diagnosis', string='')
    treatment_id = fields.Many2one('airport.medical.treatment', string='處置')
    result_id = fields.Many2one('airport.medical.result', string='結果')
    treatment_hospital_id = fields.Many2one('airport.medical.treatment.hospital', string='若在醫院的處置')
    personal_opinion = fields.Text(string='個人意見')
    notification_time = fields.Datetime(default=lambda self: fields.Datetime.now(), string='通報時間')
    def refresh_time(self):
        self.notification_time = fields.Datetime.now()
    clinic_time = fields.Datetime(default=lambda self: fields.Datetime.now(), string='診療時間')
    def refresh_time1(self):
        self.clinic_time = fields.Datetime.now()
    attending_physician_id = fields.Many2one('airport.medical.attending.physician', string='負責醫師')
    attending_nurse_id = fields.Many2one('airport.medical.attending.nurse', string='隨行護士')
    test1 = fields.Char(string='test')
    identity_id = fields.Many2one('airport.medical.identity', string='身分')
    password_no = fields.Char(string='護照號碼')
    Date = fields.Date(default=lambda self: fields.Date.today(), string='日期')
    Address = fields.Char(string='地址')
    Phone = fields.Char(string='聯絡電話')
    Airplane = fields.Char(string='班機')
    exit_id  = fields.Many2one('airport.medical.exit', string='出入境')
    content= fields.Text(string='內容',groups='airport.airport_group_nurse')
    current_time = fields.Datetime(string='紀錄時間', readonly=True)
    display_content = fields.Text(string='紀錄內容')
    record_count = fields.Integer(string='總記錄筆數')
    total_record_count = fields.Char(string='總紀錄筆數', compute='_compute_total_record_count')
    def record(self):
        if self.content:
            self.record_count += 1

            if not self.display_content:
                self.display_content = f"{self.record_count}. {self.content} {self.tst}"
            else:
                self.display_content += f"\n{self.record_count}. {self.content} {self.tst}"

            self.current_time = datetime.datetime.now()
            self.content = False
    def reset(self):
        if not self.display_content:
            self.content = False
        else:
            self.content = False    
        
    @api.depends('record_count')
    def _compute_total_record_count(self):
        for record in self:
            record.total_record_count = f"{record.record_count} 筆"
    doctor_remark = fields.Text(string='醫師囑言及備註')
    diagnosis_category = fields.Many2one('airport.medical.diagnosis', string='')
    diagnosis_detail = fields.Many2one('airport.medical.diagnosis')
    comment_id= fields.Many2one('airport.medical.comment', string='醫師囑言')
    comment2= fields.Many2one('airport.medical.comment')
    comment3= fields.Many2one('airport.medical.comment')
    temperature = fields.Float(string='體溫', digits=(2, 1))
    temperature_status = fields.Char(string='體溫狀態', compute='_compute_temperature_status', store=True)
    tst = fields.Selection(string='護理師',selection=[('尹淨漢', '尹淨漢'), ('全圓佑', '全圓佑'), ('王曉明', '王曉明'), ('蔡依林', '蔡依林'), ('周杰倫', '周杰倫'), ('山下智久', '山下智久')],
        help="Type is used to separate Leads and Opportunities",groups='airport.airport_group_nurse')
    @api.onchange('temperature')
    def _onchange_temperature(self):
        if self.temperature and int(self.temperature) > 99:
            raise ValidationError('不能輸入超過兩位整數！')
    @api.depends('temperature')
    def _compute_temperature_status(self):
        for record in self:
            if record.temperature and record.temperature <= 37.5:
                record.temperature_status = '體溫正常'
            elif record.temperature and record.temperature > 37.5:
                record.temperature_status = '體溫異常'
            else:
                record.temperature_status = ''
    pulse = fields.Char(string='脈搏')
    breath = fields.Char(string='呼吸')
    blood_pressureh = fields.Char(string='血壓')
    blood_oxygen = fields.Char(string='血氧') 
    consciousness = fields.Char(string='意識', readonly=True) 
    allergy = fields.Char(string='藥物過敏', readonly=True) 
    is_active1 = fields.Boolean(string='Clear')
    is_active2 = fields.Boolean(string='GCS')
    is_active3 = fields.Boolean(string="無")
    is_active4 = fields.Boolean(string="有")
    input_field = fields.Char(string="藥物名稱")
    head = fields.Char(string="頭頸部")
    chest = fields.Char(string="胸部")
    abdomen = fields.Char(string="腹部")
    limbs = fields.Char(string="四肢")
    other = fields.Char(string="其他")
    # sherry
    assistscreening = fields.Boolean(string="協助篩檢")
    throat = fields.Boolean(string="喉嚨採檢")
    blood = fields.Boolean(string="抽血採檢")
    otheropinion = fields.Boolean(string="其他")
    otheropinionname = fields.Char(string="名稱")
    relation = fields.Char(string="關係")
    generally = fields.Boolean(string="一般通關")
    urgent = fields.Boolean(string="緊急通關")
    businessdoor = fields.Boolean(string="公務門")
    apron = fields.Boolean(string="機坪")
    medicalcenter = fields.Boolean(string="醫療中心")
    folk = fields.Boolean(string="民間")
    folkyesno = fields.Char(string="民間名稱")
    firebrigade = fields.Boolean(string="消防隊")
    firebrigadeyesno = fields.Char(string="消防隊名稱")
    transferhospital = fields.Char(string="轉送醫院")
    carattendant = fields.Char(string="隨車人員")
    visitfee = fields.Char(string="初診費")
    ambulancefee = fields.Char(string="救護車費用")
    selfpay = fields.Boolean(string="自付")
    selfpayyes = fields.Char(string="費用")
    pleasepay = fields.Boolean(string="請款")
    pleasepayyes = fields.Char(string="費用")
    cash = fields.Boolean(string="現金")
    twd = fields.Boolean(string="台幣")
    othercurrencies = fields.Boolean(string="其他幣別")
    currencies = fields.Char(string="幣別")
    afterexchange = fields.Char(string="兌換後")
    creditcard = fields.Boolean(string="刷卡")
    abnormal = fields.Boolean(string="收費異常")
    abnormalreason = fields.Char(string="原因")
    applicant = fields.Char(string="申請人")
    applicantunit = fields.Char(string="申請單位")
    phonenumber = fields.Char(string="電話")
    agreeperson = fields.Binary(string="同意簽")
    agreeperson1 = fields.Binary(string="同意簽")
    witness = fields.Binary(string="見證簽")
    witness1 = fields.Binary(string="見證簽")
    emt = fields.Char(string="emt")
     # 廖庭萱
    landing_time_yesno = fields.Boolean(string='是')
    landing_time = fields.Datetime(string='落地時間', default=lambda self: fields.Datetime.now())
    def refresh_landing_time(self):
        self.landing_time = fields.Datetime.now()
    informing_time = fields.Datetime(string='通報時間', default=lambda self: fields.Datetime.now())
    def refresh_informing_time(self):
        self.informing_time = fields.Datetime.now()
    reporting_unit = fields.Char(string="通報單位")
    reporting_unit_personnel = fields.Char(string="通報單位人員")
    reporting_unit_personnel_phone = fields.Char(string="電話")
    inform_campingoffice_time = fields.Datetime(string='通知營安處時間', default=lambda self: fields.Datetime.now(),readonly=False)
    def refresh_campingoffice_time(self):
        self.inform_campingoffice_time = fields.Datetime.now()
    arrive_yesno = fields.Char(string='是否到達現場')
    is_active5 = fields.Boolean(string="是")
    is_active6 = fields.Boolean(string="否")
    is_active7 = fields.Boolean(string="T1")
    active7_yes = fields.Char(string='T1名稱')
    is_active8 = fields.Boolean(string="T2")
    active8_yes = fields.Char(string='T2名稱')
    informing_place = fields.Char(string='通報事故地點')
    informing_place_input_field = fields.Char(string="其他地點")
    arriving_time = fields.Datetime(string='醫護抵達時間', default=lambda self: fields.Datetime.now(),readonly=False)
    def refresh_arriving_time(self):
        self.arriving_time = fields.Datetime.now()
    arrive_in10mins = fields.Char(string="是否十分鐘內抵達")
    is_active9 = fields.Boolean(string="是")
    is_active10 = fields.Boolean(string="否")
    arrive_in10mins_input_field =  fields.Char(string="原因")
    checking_time = fields.Datetime(string='檢查時間', default=lambda self: fields.Datetime.now())
    def refresh_checking_time(self):
        self.checking_time = fields.Datetime.now()
    sup_sign=fields.Binary(string="院長簽名")
    doctor_sign=fields.Binary(string="診治醫師簽名")
    icd10_category_id=fields.Many2one('airport.medical.icd10.category')
    icd10_category1_id=fields.Many2one('airport.medical.icd10.category1')
    icd10_category2_id=fields.Many2one('airport.medical.icd10.category2')
    icd10_category3_id=fields.Many2one('airport.medical.icd10.category3')
    icd10_category4_id=fields.Many2one('airport.medical.icd10.category4')
    icd10_category5_id=fields.Many2one('airport.medical.icd10.category5')
    icd10_category6_id=fields.Many2one('airport.medical.icd10.category6')
    icd10_category7_id=fields.Many2one('airport.medical.icd10.category7')
    icd10_category8_id=fields.Many2one('airport.medical.icd10.category8')
    icd10_category9_id=fields.Many2one('airport.medical.icd10.category9')
    icd10_category10_id=fields.Many2one('airport.medical.icd10.category10')
    icd10_category11_id=fields.Many2one('airport.medical.icd10.category11')
    icd10_category12_id=fields.Many2one('airport.medical.icd10.category12')
    icd10_category13_id=fields.Many2one('airport.medical.icd10.category13')
    icd10_category18_id=fields.Many2one('airport.medical.icd10.category18')
    initial_diagnosis_icd10=fields.Many2one('airport.medical.icd10')
    Quadruple_single=fields.Boolean(string="簽四聯單")
    referral=fields.Boolean(string="建議轉診")
    photo = fields.Binary(string='上傳照片')
    photo1 = fields.Binary(string='')
    input_field_hospital =  fields.Char(string="轉診醫院")
    input_field_E = fields.Selection(string='睜眼反應',selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')],
                                         help="Type is used to separate Leads and Opportunities")
    
    input_field_V =  fields.Selection(string="語言反應",selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
                                         help="Type is used to separate Leads and Opportunities")
    
    input_field_M =  fields.Selection(string="動作反應",selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')],
                                         help="Type is used to separate Leads and Opportunities")
    total_score = fields.Integer(string="昏迷指數總分", compute="_compute_total_score", store=True)
    comatose_level = fields.Char(string="昏迷程度", compute="_compute_comatose_level", store=True)
    allergy1 = fields.Char(string='過去病史', readonly=True) 
    is_no = fields.Boolean(string="無")
    is_yes = fields.Boolean(string="有")
    input_field1 = fields.Char(string="過去病史名稱")
    
    def button_add_info(self):
        return{
            'type':'ir.actions.act_window',
            'res_model':'image.capture',
            'name':'護照掃描',
            'view_mode':'form',
            'target':'new',
        }
    

    @api.depends('input_field_E', 'input_field_V', 'input_field_M')
    def _compute_total_score(self):
        for record in self:
            score_E = int(record.input_field_E) if record.input_field_E else 0
            score_V = int(record.input_field_V) if record.input_field_V else 0
            score_M = int(record.input_field_M) if record.input_field_M else 0
            record.total_score = score_E + score_V + score_M

    @api.depends('total_score')
    def _compute_comatose_level(self):
        for record in self:
            if 13 <= record.total_score <= 15:
                record.comatose_level = '輕微昏迷'
            elif 9 <= record.total_score <= 12:
                record.comatose_level = '中度昏迷'
            elif 3 <= record.total_score <= 8:
                record.comatose_level = '重度昏迷'
            else:
                record.comatose_level = ''

    @api.model
    def create_or_update_from_image_capture(self, data):
        _logger = logging.getLogger(__name__)

        # 提取数据字段
        name = data.get('name')
        birthday = data.get('birthday')
        passport_number = data.get('password_no')

        # 检查是否已存在具有相同姓名的记录
        #existing_record = self.search([('name', '=', name)], limit=1)

        #if existing_record:
            # 如果找到匹配的记录，更新字段
            
        self.write({
            'name':name,
            'birthday': birthday,
            'password_no': passport_number,
        })
        _logger.info('Record updated successfully for name: %s', name)
        

        return 


    bill_id = fields.Many2one('airport.medical.bill',string='帳單')

    @api.model
    def create(self, vals):
        # 创建出診單记录
        medical_record = super(AirportMedical, self).create(vals)

        # 创建帳單记录
        medical_data = {
            'name': medical_record.name,
            'Date': fields.Date.today(),
            'visitfee': medical_record.visitfee,
            'ambulancefee': medical_record.ambulancefee,
            'pleasepay': medical_record.pleasepay,
            'cash': medical_record.cash,
            'creditcard': medical_record.creditcard,
            'medical_ids': [(4, medical_record.id)]  # 正确的方式来关联记录
        }
        medical_bill = self.env['airport.medical.bill'].create(medical_data)

        if not medical_record.name:
            bill_to_delete = self.env['airport.medical.bill'].search([('medical_ids', '=', medical_record.id)])
            bill_to_delete.unlink()

        return medical_record

    @api.depends('name', 'visitfee', 'ambulancefee', 'pleasepay', 'cash', 'creditcard')
    def _update_medical_bills(self):
        for medical in self:
            for bill in medical.bill_id:
                bill.write({
                    'name': medical.name,
                    'visitfee': medical.visitfee,
                    'ambulancefee': medical.ambulancefee,
                    'pleasepay': medical.pleasepay,
                    'cash': medical.cash,
                    'creditcard': medical.creditcard,
                })

    def write(self, vals):
        res = super(AirportMedical, self).write(vals)
        if vals:
            self._update_medical_bills()
        return res


   
    
