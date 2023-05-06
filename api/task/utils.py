# coding=utf-8

import datetime
import traceback
import re
from api.common.logger import logger


def equation(value1, value2):
    if str(value1) == str(value2):
        return True
    else:
        return False


def f_equation(value1, value2):
    try:
        if "".join(str(value1).split()).isalpha():
            value1 = word_to_number(value1)
        if "".join(str(value2).split()).isalpha():
            value1 = word_to_number(value2)
        if float(value1) == float(value2):
            return True
        else:
            return False
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def lg(value1, value2):
    try:
        if "".join(str(value1).split()).isalpha():
            value1 = word_to_number(value1)
        if "".join(str(value2).split()).isalpha():
            value1 = word_to_number(value2)
        if float(value1) > float(value2):
            return True
        else:
            return False
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def lt(value1, value2):
    try:
        if "".join(str(value1).split()).isalpha():
            value1 = word_to_number(value1)
        if "".join(str(value2).split()).isalpha():
            value1 = word_to_number(value2)
        if float(value1) < float(value2):
            return True
        else:
            return False
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def is_in(value1, value2):
    if str(value1) in str(value2):
        return True
    else:
        return False


def is_contains(value1, value2):
    if str(value2) in str(value1):
        return True
    else:
        return False


def before(value1, value2):
    try:
        print(value1, value2)
        value1 = re.sub(r'[\u4e00-\u9fa5]+', "", value1)
        value2 = re.sub(r'[\u4e00-\u9fa5]+', "", value2)
        if value1.isdigit() and value2.isdigit():
            if int(value1) < int(value2):
                return True
            else:
                return False
        if re.match(r"^\d+-\w+-\d+$", value1) is not None:
            strftime1 = datetime.datetime.strptime(value1, "%d-%b-%y")
        elif re.match(r"^\w+\.\d+,\d+$", value1) is not None:
            strftime1 = datetime.datetime.strptime(value1, "%b.%d,%Y")
        else:
            strftime1 = datetime.datetime.strptime(value1, "%Y-%m-%d %H:%M:%S")
        if re.match(r"^\d+-\w+-\d+$", value2) is not None:
            strftime2 = datetime.datetime.strptime(value2, "%d-%b-%y")
        elif re.match(r"^\w+\.\d+,\d+$", value2) is not None:
            strftime2 = datetime.datetime.strptime(value2, "%b.%d,%Y")
        else:
            strftime2 = datetime.datetime.strptime(value2, "%Y-%m-%d %H:%M:%S")

        if strftime1 < strftime2:
            return True
        else:
            return False
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def after(value1, value2):
    try:
        value1 = re.sub(r'[\u4e00-\u9fa5]+', "", value1)
        value2 = re.sub(r'[\u4e00-\u9fa5]+', "", value2)
        if value1.isdigit() and value2.isdigit():
            if int(value1) > int(value2):
                return True
            else:
                return False
        if re.match(r"^\d+-\w+-\d+$", value1) is not None:
            strftime1 = datetime.datetime.strptime(value1, "%d-%b-%y")
        elif re.match(r"^\w+\.\d+,\d+$", value1) is not None:
            strftime1 = datetime.datetime.strptime(value1, "%b.%d,%Y")
        else:
            strftime1 = datetime.datetime.strptime(value1, "%Y-%m-%d %H:%M:%S")
        if re.match(r"^\d+-\w+-\d+$", value2) is not None:
            strftime2 = datetime.datetime.strptime(value2, "%d-%b-%y")
        elif re.match(r"^\w+\.\d+,\d+$", value2) is not None:
            strftime2 = datetime.datetime.strptime(value2, "%b.%d,%Y")
        else:
            strftime2 = datetime.datetime.strptime(value2, "%Y-%m-%d %H:%M:%S")
        if strftime1 > strftime2:
            return True
        else:
            return False
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def findValByKey(key, data):
    if isinstance(data, list):
        for item in data:
            ret = findValByKey(key, item)
            if ret is not None:
                return ret
    elif isinstance(data, dict):
        for k, v in data.items():
            if key == k:
                return v
            else:
                ret = findValByKey(key, v)
                if ret is not None:
                    return ret


_known = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}


def word_to_number(n):
    """

    :param n:
    :return:
    """
    en_digit = []
    for k, v in _known.items():
        en_digit.append(k)
    en_digit = list(reversed(en_digit))
    en_digit.append("only")
    replace_content = {item: f"{item} " for item in en_digit}
    replace_content.update({"only": ""})
    regex = re.compile("|".join(en_digit))
    _result = regex.sub(
        lambda m: replace_content[re.escape(m.group(0))],
        str(n).lower()
    )
    n = " ".join(_result.split())
    # *********
    n = n.lower().strip()
    if n in _known:
        return _known[n]
    else:
        inputWordArr = re.split('[ -]', n)
    assert len(inputWordArr) > 1
    if inputWordArr[-1] == 'hundred':
        inputWordArr.append('zero')
        inputWordArr.append('zero')
    if inputWordArr[-1] == 'thousand':
        inputWordArr.append('zero')
        inputWordArr.append('zero')
        inputWordArr.append('zero')
    if inputWordArr[0] == 'hundred':
        inputWordArr.insert(0, 'one')
    if inputWordArr[0] == 'thousand':
        inputWordArr.insert(0, 'one')
    inputWordArr = [word for word in inputWordArr if word not in ['and', 'minus', 'negative']]
    currentPosition = 'unit'
    output = 0
    for word in reversed(inputWordArr):
        if currentPosition == 'unit':
            number = _known[word]
            output += number
            if number > 9:
                currentPosition = 'hundred'
            else:
                currentPosition = 'ten'
        elif currentPosition == 'ten':
            if word != 'hundred':
                number = _known[word]
                if number < 10:
                    output += number * 10
                else:
                    output += number
            currentPosition = 'hundred'
        elif currentPosition == 'hundred':
            if word not in ['hundred', 'thousand']:
                number = _known[word]
                output += number * 100
                currentPosition = 'thousand'
            elif word == 'thousand':
                currentPosition = 'thousand'
            else:
                currentPosition = 'hundred'
        elif currentPosition == 'thousand':
            assert word != 'hundred'
            if word != 'thousand':
                number = _known[word]
                output += number * 1000
        else:
            assert "Can't be here" == None
    return output


if __name__ == '__main__':
    dd = {'taskInfoId': None, 'processId': 'd7fd139a91dc4a5994778308040a2dc8',
          'callbackId': 'cbac10fd36854d2b8f0d76becc0bd8e4', 'processName': '城保参保单位',
          'processTaskId': '91cc4665c7f345219d29d25805d0326b', 'processTaskName': '城保参保单位人员减少',
          'templates': 'd6c7d82d344540d1b6511f6c627cd77d', 'templateNo': 1, 'configs': [
            {'configId': 'a4fec380bfed4819b5b26366304c7a52', 'configName': 'task_monitoring', 'configAilas': '任务监听',
             'config': {'businessInformation': [{'url': 'http://10.10.50.10/portal/',
                                                 'identification': '/html/body/div/div/div[2]/section/div/div[1]/div[1]/div/div/div/div[contains(@class,"is-active")]/span[1]'}]},
             'result': {}},
            {'configId': '3f44959805a34b9e9a247bf1f8596b67', 'configName': 'naming_rule', 'configAilas': '命名设定',
             'config': {'result_varname': 'ipa_name_mod', 'naming_mode': {'name': 'time_stamp', 'value': '14'}},
             'result': {'ipa_name_mod': '23471129268'}},
            {'configId': 'c8e6b62e59124f5186024c42ff8855e6', 'configName': 'file_migration', 'configAilas': '文件迁移',
             'config': {'origin_path': 'D:\\gaopaiyi', 'out_path': 'D:\\MBLJ', 'name': 'custom',
                        'result_tips_varname': 'ipa_remove_result',
                        'migration_mode': {'name': 'custom', 'value': 'ipa_name_mod'}},
             'result': {'origin_path': 'D:\\gaopaiyi', 'ipa_remove_result': 'D:\\MBLJ\\23471129268'}},
            {'configId': 'e32fa97ad1934eae8bf13e6ed9c356e0', 'configName': 'hc_image_process', 'configAilas': '高拍仪图像处理',
             'config': {'root_path': 'D:\\data', 'dir_path': '', 'dir_name': 'ipa_remove_result',
                        'automate': 'text_direction', 'tips_varname': 'rpa_img_result01',
                        'export_image': {'type': 'cover', 'image_path': ''}}, 'result': {
                '91cc4665c7f345219d29d25805d0326b': {
                    1676509364308: {'origin_path': 'D:\\MBLJ\\temp\\23471129268\\20230216090243.jpg',
                                    'handled_path': 'D:\\MBLJ\\23471129268\\20230216090243.jpg'}}}},
            {'configId': 'b2fef30260c94017943d018ec9501eb6', 'configName': 'image_identification',
             'configAilas': '图像鉴别', 'config': {'root_path': 'D:\\data', 'dir_path': '', 'dir_name': 'ipa_remove_result',
                                               'required_category': ['重庆市参加社会保险单位人员减少申报表.png'],
                                               'required_tips_varname': 'rpa_chk_result01',
                                               'required_display_category': '缺少类别名',
                                               'required_prompt_content': '[rpa_chk_content01]是必须的',
                                               'optional_category': [], 'optional_tips_varname': 'rpa_chk_result02',
                                               'optional_display_category': '缺少可选类别名',
                                               'optional_prompt_content': '[rpa_chk_content02]是可选的。',
                                               'summary_tips_varname': '222',
                                               'summary_prompt_content': '[rpa_chk_result01][rpa_chk_result02]',
                                               'result_tips_varname': 'rpa_chk_out01',
                                               'examine_counts': 'rpa_chk_count', 'error_counts': 'rpa_chk_error',
                                               'required_category_varname': 'rpa_chk_content01',
                                               'optional_category_varname': 'rpa_chk_content02'},
             'result': {'rpa_chk_result01': '', 'rpa_chk_result02': '', '222': '',
                        'rpa_chk_out01': {'success': True, 'business_name': '城保参保单位人员减少', 'username': '夏丽',
                                          'created': '2023-02-16 09:02:45', 'rpa_chk_count': 0, 'rpa_chk_error': 0,
                                          'img_success': [{'file_name': '20230216090243.jpg',
                                                           'file_path': 'D:\\MBLJ\\temp\\23471129268\\20230216090243.jpg',
                                                           'file_key': 'a4be81178b853828f1c55bba3f5fccec',
                                                           'category': ['重庆市参加社会保险单位人员减少申报表']}], 'img_error': [],
                                          'error_msg': ''}}},
            {'configId': 'a444917ede0b48e29130912c67f6f7e9', 'configName': 'interface_prompt', 'configAilas': '界面提示',
             'config': {'prompt_mode': 'popup_prompt', 'popup_prompt': '222'}, 'result': {}},
            {'configId': '7f8a0c0149d94702988731206b3312d7', 'configName': 'image_quality', 'configAilas': '图像质检',
             'config': {'root_path': 'D:\\data', 'dir_path': '', 'dir_name': 'ipa_remove_result',
                        'tips_varname': 'rpa_qa_result01'},
             'result': {'rpa_qa_result01': {'success': True, 'error_msg': ''}}},
            {'configId': '3d1830e377014d789e418d9b7ba4d4c4', 'configName': 'message_sync', 'configAilas': '消息同步',
             'config': {'result_varname': 'rpa_msg_result01', 'prompt_content': '123',
                        'tips_varname': 'rpa_msg_content01', 'return_prompt': 'rpa_chk_out01',
                        'identification': '/html/body/div[1]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/button[2]/span'},
             'result': {'rpa_msg_result01': '123',
                        'rpa_msg_content01': {'success': True, 'business_name': '城保参保单位人员减少', 'username': '夏丽',
                                              'created': '2023-02-16 09:02:45', 'rpa_chk_count': 0, 'rpa_chk_error': 0,
                                              'img_success': [{'file_name': '20230216090243.jpg',
                                                               'file_path': 'D:\\MBLJ\\temp\\23471129268\\20230216090243.jpg',
                                                               'file_key': 'a4be81178b853828f1c55bba3f5fccec',
                                                               'category': ['重庆市参加社会保险单位人员减少申报表']}], 'img_error': [],
                                              'error_msg': ''}}}], 'processTaskType': '城保参保单位人员减少'}

    ret = findValByKey("optional_display_category", dd)
    print(ret)
    # ret = findValInDict("城保参保单位人员减少", dd)
    # print(ret)

    [{"信用证编号": [{"bbox": [[325, 520, 341, 546],
                          [409, 518, 609, 544],
                          [695, 518, 745, 546]],
                 "end": 258,
                 "probability": 0.9985132887244674,
                 "start": 244,
                 "text": ".DRO-LOLC01Dat"}],
      "大写汇票金额": [{"bbox": [[962, 403, 985, 429], [49, 464, 101, 486]],
                  "end": 215,
                  "probability": 0.6392853227792656,
                  "start": 212,
                  "text": "DTT"}],
      "小写汇票金额": [{"bbox": [[420, 173, 597, 199]],
                  "end": 70,
                  "probability": 0.9995687264546405,
                  "start": 60,
                  "text": "US$1237.00"}],
      "开证日期": [{"bbox": [[812, 518, 947, 546], [43, 574, 114, 609]],
                "end": 274,
                "probability": 0.9987236242042563,
                "start": 262,
                "text": "4-Apr-01Issu"}],
      "开证行": [{"bbox": [[185, 574, 203, 609],
                        [284, 577, 887, 602],
                        [45, 632, 111, 663]],
               "end": 311,
               "probability": 0.9912971534848758,
               "start": 278,
               "text": "yBANK OF CHINA SHANGHAIBRANCHValu"}],
      "汇票序号": [{"bbox": [[642, 231, 782, 262]],
                "end": 94,
                "probability": 0.9992384592550252,
                "start": 84,
                "text": "this FIRST"}],
      "汇票日期": [{"bbox": [[354, 346, 618, 372], [47, 403, 92, 429]],
                "end": 174,
                "probability": 0.6315741849411012,
                "start": 160,
                "text": "AISHANG BANKth"},
               {"bbox": [[859, 115, 1024, 146]],
                "end": 44,
                "probability": 0.9655450944582071,
                "start": 35,
                "text": "27-May-01"}],
      "货物数量": [{"bbox": [[259, 632, 276, 663],
                         [317, 635, 458, 662],
                         [42, 687, 65, 724]],
                "end": 330,
                "probability": 0.9951631801627698,
                "start": 320,
                "text": "d600 SETST"}]}]
