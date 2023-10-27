# -*- coding: utf-8 -*-
from odoo import fields, models, api
import cv2
import pytesseract
import base64
import os
import logging
import numpy as np
import re
from passporteye import read_mrz

class ImageCapture(models.TransientModel):
    _name = 'image.capture'
    _description = 'Image Captures'

    name = fields.Char(string='Name', help='Name of the image to capture')
    ocr_result = fields.Text(string='OCR Result', help='OCR result', readonly=True)
    mrz_result = fields.Text(string='MRZ Result', help='MRZ result', readonly=True)
    source_model = fields.Char(string='Source Model', help='Source model name', readonly=True)

    @api.model
    def action_save_image(self, image_data):
        _logger = logging.getLogger(__name__)
        try:
            # 解码图像数据
            image_data = image_data.split(',')[1].strip()
            image_bytes = base64.b64decode(image_data)

            # 保存图像文件
            image_path = 'C:/Users/user/Desktop/odoo16/server/odoo/addons/airport/static/img/captured_image.jpg'
            with open(image_path, 'wb') as img_file:
                img_file.write(image_bytes)

            if os.path.exists(image_path):
                # 执行OCR
                image = cv2.imread(image_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = image.astype(np.uint8)

                # 图像预处理
                enhanced_image = (image * 1.5).astype(np.uint8)
                denoised_image = cv2.fastNlMeansDenoisingColored(enhanced_image, None, 10, 10, 7, 21)
                gray_image = cv2.cvtColor(denoised_image, cv2.COLOR_BGR2GRAY)
                _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

                ocr_text = pytesseract.image_to_string(binary_image, lang='chi_tra+eng')

                # 使用passporteye解析MRZ文本
                mrz_data = read_mrz(image_path)
                if mrz_data:
                    ocr_text += f'\n\nMRZ Data:\n{mrz_data}'

                    # 记录OCR和MRZ结果
                    _logger.info(f'OCR Result in action_save_image: {ocr_text}')
                    _logger.info(f'MRZ Data: {mrz_data}')

                    # 分解MRZ数据并按需求显示
                    passport_type = mrz_data.type.replace("<", "")
                    passport_number = mrz_data.number
                    fullname = mrz_data.names.replace('<', ' ').replace('K', ' ').strip()
                    surname = mrz_data.surname  # 删除 "K" 字符
                    country_code_and_issuer = mrz_data.country
                    gender = mrz_data.sex
                    birth_date = mrz_data.date_of_birth

                    # 进一步分割国家代码和发行者字段
                    country_code_and_issuer = mrz_data.country
                    if ' ' in country_code_and_issuer:
                        country_code, issuer = country_code_and_issuer.split(' ')
                    else:
                        country_code = country_code_and_issuer
                    issuer = ""  # 或者将其设置为适当的默认值
                    # 构建MRZ结果字符串
                    # 处理名字和姓氏字段
                    # 初始化名字和姓氏字段
                    fullname = ""
                    surname = ""

                    if hasattr(mrz_data, 'names'):
                        names = mrz_data.names.split('<')
                        if len(names) >= 2:
                            surname = names[0].strip().replace('K', '').strip()
                            fullname = names[1].strip().replace('K', '').strip()
                        elif len(names) == 1:
                            # 如果只有一个姓名字段，则将其作为名字
                            fullname = names[0].strip().replace('K', '').strip()
                            _logger.info("fullname")


                    # 使用 'surname' 和 'name' 变量来获取姓和名

                
                # 获取护照号码
                passport_number = ""
                if hasattr(mrz_data, 'number'):
                    passport_number = mrz_data.number


                # 假设您想要设置默认值 "Unknown" 作为护照类型
                passport_type = "Unknown"

                # 检查是否存在 mrz_data，并且 mrz_data.type 是否存在
                if mrz_data and hasattr(mrz_data, 'type'):
                    passport_type = mrz_data.type

                
                mrz_result = f"Passport Type: {passport_type}\nPassport Number: {passport_number}\nName:{surname} {fullname}\nCountry Code: {country_code}\nGender: {gender}\nBirth Date: {birth_date}"

                # 将OCR结果和其他信息保存到当前记录
                self.write({
                    'ocr_result': ocr_text,
                    'mrz_result': mrz_result
                })

                # 清理 - 删除临时图像文件
                os.remove(image_path)

                # 记录OCR结果
                _logger.info(f'OCR Result in action_save_image: {ocr_text}')
                _logger.info(f'MRZ Result in action_save_image: {mrz_result}')

            else:
                raise Exception("Failed to save image file.")

            return {'success': True, 'message': 'Image saved successfully', 'ocr_result': ocr_text}
        except Exception as e:
            _logger.error(f'Error: {str(e)}')
            return {'success': False, 'error': str(e)}
