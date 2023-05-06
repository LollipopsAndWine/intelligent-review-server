import requests


class HttpClient:
    def __init__(self):
        """
        session管理器
        requests.session(): 维持会话,跨请求的时候保存参数
        """
        # 实例化session
        self.session = requests.session()

    def request_api(self, method, _url, params=None, data=None, json=None, headers=None, **kwargs):
        """

        :param method: 请求方式
        :param _url: 请求地址
        :param params: 字典或bytes，作为参数增加到url中
        :param data: data类型传参，字典、字节序列或文件对象，作为Request的内容
        :param json: json传参，作为Request的内容
        :param headers: 请求头，字典
        :param kwargs: 若还有其他的参数，使用可变参数字典形式进行传递
        :return:
        """
        re_data = self.session.request(method, _url, params=params, data=data, json=json, headers=headers,
                                       verify=False, **kwargs)

        # 返回响应结果
        return re_data


hc = HttpClient()

if __name__ == '__main__':
    # 请求地址
    url = 'http://127.0.0.1:8085/ai/ic'
    # 请求参数
    payload = {
        "targetPath": "D:/Work/PycharmProjects/pythonProject/web/huntsman/kubaoAi/kubaoai/ai_services/demo.jpeg"
    }
    # 请求头
    header = {}
    # 实例化 RequestMain()
    hc = HttpClient()
    # 调用request_main，并将参数传过去
    request_data = hc.request_api("POST", url, json=payload, headers=header)
    # 打印响应结果
    print(request_data.json())

