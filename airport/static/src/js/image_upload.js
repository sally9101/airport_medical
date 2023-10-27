/** @odoo-module */

import { registry } from '@web/core/registry';

import { formView } from '@web/views/form/form_view';
import { FormController } from '@web/views/form/form_controller';
import { FormRenderer } from '@web/views/form/form_renderer';
const { useListener } = require("@web/core/utils/hooks");
//import rpc from 'web.rpc';
import { patch } from "@web/core/utils/patch";

// 在 autoFillOcrResult 函数外部声明一个变量来存储当前记录的 ID
const currentRecordId = parseInt(new URLSearchParams(window.location.hash.substring(1)).get('id'));

// 确保成功获取了记录的 ID
if (!isNaN(currentRecordId)) {
    // 在这里可以使用 currentRecordId 进行后续操作
    console.log('Current Record ID:', currentRecordId);
} else {
    console.error('Failed to retrieve current Record ID.');
}

// 检查日期的有效性
function isValidDate(dateString) {
    const regEx = /^\d{4}-\d{2}-\d{2}$/;
    if (!dateString.match(regEx)) return false;  // 格式无效
    const d = new Date(dateString);
    if (!d.getTime() && d.getTime() !== 0) return false; // 日期无效
    return d.toISOString().slice(0, 10) === dateString;
}

// 获取 URL 中的参数值
function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    const regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)');
    const results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

patch(FormRenderer.prototype, 'FormRender',{
    setup() {
        this._super();
    },
    async OnClickOpenCamera() {
        var player = document.getElementById('player');
        var captureButton = document.getElementById('capture');
        var camera = document.getElementById('camera');
        const formId = getParameterByName('id');
    
        // 检查是否已经有摄像头流正在播放
        if (player.srcObject) {
            const tracks = player.srcObject.getTracks();
            tracks.forEach(function (track) {
                track.stop();
            });
        }
    
        player.classList.remove('d-none');
        captureButton.classList.remove('d-none');
        camera.classList.add('d-none');
        
        let stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
        player.srcObject = stream;

        // 使用表单ID执行其他操作
        if (formId !== null) {
            console.log('Form ID:', formId);
            // 在这里可以使用 formId 进行其他操作
        } else {
            console.log('ID parameter not found in the URL.');
        }
    },

    async OnClickChangeCamera() {
        const videoElement = document.getElementById('player');
    const currentStream = videoElement.srcObject;
    if (!currentStream) {
        console.error('No video stream to switch.');
        return;
    }

    const tracks = currentStream.getTracks();
    for (const track of tracks) {
        track.stop();
    }

    const facingMode = videoElement.getAttribute('data-facing-mode');
    const newFacingMode = facingMode === 'user' ? 'environment' : 'user';

    try {
        const newStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: newFacingMode }, audio: false });
        videoElement.srcObject = newStream;
        videoElement.setAttribute('data-facing-mode', newFacingMode);
    } catch (error) {
        console.error('Error switching camera:', error);
    }
},
    
      

    async OnClickCloseCamera() {
        // 添加关闭相机的按钮的点击事件处理程序
        var closeButton = document.getElementById('close_camera');
        var captureButton = document.getElementById('capture');
        var camera = document.getElementById('camera');

        closeButton.addEventListener('click', function () {
            // 关闭摄像头流
            var player = document.getElementById('player');
            var stream = player.srcObject;
            var tracks = stream.getTracks();
            tracks.forEach(function (track) {
                track.stop();
            });

            // 隐藏相关元素
            player.classList.add('d-none');
            captureButton.classList.add('d-none');
            camera.classList.remove('d-none');

        });

    },
    async OnClickCaptureImage() {
        // Capture the image from webcam and close the webcam
        var context = snapshot.getContext('2d');
        var canvas = document.getElementById('snapshot')
        var save_image = document.getElementById('save_image')
        var image = document.getElementById('image');
        var video = document.getElementById('video')
        var camera = document.getElementById('camera');
        save_image.classList.remove('d-none');
        context.drawImage(player, 0, 0, 320, 240);
        image.value = context.canvas.toDataURL();
        canvas.classList.remove('d-none');
        this.url = context.canvas.toDataURL()
    },
    async OnClickSaveImage() {
        try {
            var image = document.getElementById('image');
            var image_data = image.value;
            var rpc = require('web.rpc');
    
            // 发送保存图像请求
            const results = await rpc.query({
                model: 'image.capture',
                method: 'action_save_image',
                args: [image_data],
                context: {
                    'default_source_model': 'airport.medical', // 设置来源模型为 airport.medical
                },
            });
    
            // 打印整个响应对象以进行调试
            console.log('RPC Response1:', results);
    
            // 检查是否有错误
            if (results && results.error) {
                console.error('Error:', results.error);
            } else {
                // 从results中直接获取OCR结果
                const ocrText = results.ocr_result;
                const ocrResult = results.ocr_result;
                //console.log("OCR result1:", ocrText);
    
                if (ocrText) {
                    // 使用分隔符将 OCR 和 MRZ 部分分开
                    const [ocrText, mrzText] = ocrResult.split('\n\nMRZ Data:\n');

                    // 现在 ocrText 包含 OCR 结果，mrzText 包含 MRZ 结果
                    console.log('OCR result:', ocrText);
                    console.log('MRZ result:', mrzText);

                    // 成功获取OCR结果后，可以在前端进行处理或显示
                    console.log("OCR result2:", ocrText);
                    document.getElementById('ocr_result').textContent = "OCR辨識結果: " + ocrText;
                    document.getElementById('mrz_result').textContent = "MRZ辨識結果: " + mrzText;
                    // 在此处执行其他操作，例如在页面上显示OCR结果
                    // 例如：document.getElementById('ocr_result').textContent = ocrText;

                    // 调用自动填充函数
                    //this.autoFillOcrResult();
                } else {
                    console.error('No OCR text found in the response.');
                }
            }
        } catch (error) {
            // 捕获异常并打印错误信息
            console.error('An error occurred:', error);
        }
    },

// 在autoFillOcrResult函数中使用当前计数器的值作为recordId
async autoFillOcrResult() {
    try {
        const ocrText = document.getElementById('ocr_result').textContent;
        const mrzText = document.getElementById('mrz_result').textContent; // 获取 mrzText 的值
        var rpc = require('web.rpc');

        // 获取表单ID
        let formId = getParameterByName('id');

        //解決表單資料新增問題code
        if (formId !== null) {
            console.log('Form ID:', formId);
            // 添加一个新的Ajax请求，用于删除原始表单
            const deleteResponse = await rpc.query({
                model: 'airport.medical',  // 将 'your.model' 替换为原始表单模型的名称
                method: 'unlink',    // 使用 unlink 方法删除记录
                args: [[parseInt(formId, 10)]],  // 传递要删除的记录ID
            });

            // 打印删除操作的响应以进行调试
            console.log('Delete Response:', deleteResponse);

            // 检查是否有错误
            if (deleteResponse && deleteResponse.error) {
                console.error('Error:', deleteResponse.error);
            } else {
                console.log('Record deleted successfully');
            }
            formId = (parseInt(formId, 10) + 1).toString();
            // 在这里可以使用 formId 进行其他操作
        } else {
            console.log('ID parameter not found in the URL.');
        }



        if (!ocrText && !mrzText) {
            console.error('Neither OCR nor MRZ data received.');
            return; // 不发送数据
        }

        // 使用正则表达式分割MRZ字符串
        const mrzParts = mrzText.match(/MRZ\(([^)]+)\)/);

        if (mrzParts && mrzParts.length > 1) {
            const mrzData = mrzParts[1].split(', ');

            if (mrzData.length === 6) {
                const totalChars = mrzData[0];
                const passportNumber = mrzData[1];
                const name = mrzData[3].replace(/K/g, '').replace(/ /g, '').replace(/E/g, '');
                const surname = mrzData[2].replace(/K/g, '').replace(/ /g, '').replace(/E/g, '');
                const gender = mrzData[4];
                const birthDate = mrzData[5];
                const fullname = name+""+surname;

                // 提取年、月和日
                let year = birthDate.slice(0, 2);
                const month = birthDate.slice(2, 4);
                const day = birthDate.slice(4, 6);

                // 获取当前的年份的前两位数
                const currentYear = new Date().getFullYear();
                const currentYearStr = currentYear.toString().slice(0, 2);

                // 判断年份是否需要添加前缀
                if (year.length === 2) {
                    year = (parseInt(year) < parseInt(currentYearStr)) ? '20' + year : '19' + year;
                }

                // 将年、月和日重新组合为 'yyyy-mm-dd' 格式
                const formattedBirthDate = `${year}-${month}-${day}`;

                // 打印格式化后的出生日期
                console.log('Formatted Birth Date:', formattedBirthDate);

                // 在这里可以将这些字段发送到airport.medical或进行其他处理
                console.log('Total Chars:', totalChars);
                console.log('Passport Number:', passportNumber);
                console.log('Name:', name);
                console.log('surname:', surname);
                console.log('fullname:', fullname);
                console.log('Gender:', gender);
                console.log('Birth Date:', birthDate);
            // 创建要发送的数据对象
            const data = {
                'birthday': formattedBirthDate,
                'name': fullname,
                'password_no': passportNumber, // 使用护照号码作为密码号
                
            };

            console.log("mrz data:",data);

            // 发送数据到airport.medical
            const results = await rpc.query({
                model: 'airport.medical',
                method: 'create',  // 使用create方法创建新记录
                args: [data],  // 将数据作为参数传递给create方法
            });

            // 打印整个响应对象以进行调试
            console.log('RPC Response:', results);

            // 检查是否有错误
            if (results && results.error) {
                console.error('Error:', results.error);
            } else {
                // 成功创建记录后，可以在前端进行处理或显示
                console.log('Record created successfully:', results);
                var wizard = document.querySelector('.modal-content'); // 替换为您的 wizard 类名或选择器
                if (wizard) {
                    wizard.style.display = 'none'; // 隐藏 wizard，您也可以使用其他方法来关闭
                    window.location.href = `/web#id=${formId}&cids=1&menu_id=284&action=422&model=airport.medical&view_type=form`;
                    location.reload();
                }
            }
        } else {
            console.error('MRZ data does not contain all expected fields.');
        }
        } else {
        console.error('MRZ data not found in the MRZ string.');
        }
                //ocr
        if (ocrText) {
            // 删除 OCR 文本中的冒号和空格
            const cleanedText = ocrText.replace(/\s/g, ''); // 这将删除所有空格
            console.log('Cleaned OCR text:', cleanedText);

            // 确保清理后的文本不为空
            if (cleanedText) {
                // 在不同字段之间添加换行符
                const formattedText = cleanedText.replace(/姓名/g, '\n姓名')
                                                  .replace(/性別/g, '\n性別')
                                                  .replace(/國籍/g, '\n國籍')
                                                  .replace(/生日/g, '\n生日')
                                                  .replace(/護照號碼/g, '\n護照號碼');

                console.log('Formatted OCR text:', formattedText);

                // 提取姓名
                const nameMatch = formattedText.match(/姓名([\u4e00-\u9fa5a-zA-Z]+)/);
                const name = nameMatch ? nameMatch[1].trim() : '';

                // 提取性别
                const sexMatch = formattedText.match(/性別([\u4e00-\u9fa5a-zA-Z]+)/);
                const sex = sexMatch ? sexMatch[1].trim() : '';

                // 提取国籍
                const nationalityMatch = formattedText.match(/國籍([\u4e00-\u9fa5a-zA-Z]+)/);
                const nationality = nationalityMatch ? nationalityMatch[1].trim() : '';

                // 提取生日
                const birthdayMatch = formattedText.match(/生日([\d/]+)/);
                const birthday = birthdayMatch ? birthdayMatch[1].trim() : '';

                // 提取护照号码
                const passwordNoMatch = formattedText.match(/護照號碼([\w]+)/);
                const passwordNo = passwordNoMatch ? passwordNoMatch[1].trim() : '';

                // 原始日期字符串
                const originalDateStr = birthday;

                // 将日期字符串转换为 Date 对象
                const dateObj = new Date(originalDateStr);

                // 提取年、月和日
                const year = dateObj.getFullYear(); // 提取完整的四位年份
                const month = (dateObj.getMonth() + 1).toString().padStart(2, '0'); // 月份需要补零
                const day = dateObj.getDate().toString().padStart(2, '0'); // 日需要补零

                // 格式化日期为 'yyyy-mm-dd' 格式
                const formattedDateStr = `${year}-${month}-${day}`;

                console.log('Formatted Date:', formattedDateStr);


                const data = {
                    'birthday': formattedDateStr,
                    'name': name,
                    'password_no': passwordNo,

                };

                console.log('Data to be sent to airport.medical:', data);

        // 发送数据到airport.medical
        const results = await rpc.query({
            model: 'airport.medical',
            method: 'create',  // 使用create方法创建新记录
            args: [data],  // 将数据作为参数传递给create方法
        });

        // 打印整个响应对象以进行调试
        console.log('RPC Response:', results);

        // 检查是否有错误
        if (results && results.error) {
            console.error('Error:', results.error);
        } else {
            // 成功创建记录后，可以在前端进行处理或显示
            console.log('Record created successfully:', results);
            var wizard = document.querySelector('.modal-content'); // 替换为您的 wizard 类名或选择器
            if (wizard) {
                wizard.style.display = 'none'; // 隐藏 wizard，您也可以使用其他方法来关闭
                window.location.href = `/web#id=${formId}&cids=1&menu_id=284&action=422&model=airport.medical&view_type=form`;
                location.reload();
            }
            
            
        }
    } else {
        console.error('ocrText 不是有效的字符串或为空值');
    }
}else{
    console.log('error');
}
    } catch (error) {
        // 捕获异常并打印错误信息
        console.error('An error occurred while sending data to airport.medical:', error);
    }
}


});
