import requests
import GetSetting

def sendERP(url, data):
    """
    发送erp数据
    :param url:
    :param data:
    :return:
    """

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    response = requests.post(url, data=data, headers=headers)

    # print(response.text)

    # 如果是json文件可以直接显示
    # print(response.json())


if __name__ == '__main__':
    url = GetSetting.get_setting("user", "url")
    print(url)
