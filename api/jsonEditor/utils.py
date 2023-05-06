# coding=utf-8


def get_keys(data, tmp_list=[], reset=0):
    if reset == 1:
        tmp_list = []
    if isinstance(data, (list, tuple)):
        # 非字典类型，则遍历元素深入查找
        for v in data:
            get_keys(v, tmp_list)
    elif isinstance(data, dict):
        for k, v in data.items():
            print(tmp_list)
            tmp_list.append(k)
            get_keys(v, tmp_list, 0)

    return tmp_list


def NestedDictValues(d):
  for v in d.values():
    if isinstance(v, dict):
      yield from NestedDictValues(v)
    else:
      yield v


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

    ret = get_keys(dd)
    print(list(set(ret)))
    ret = NestedDictValues(dd)
    print(list(ret))
