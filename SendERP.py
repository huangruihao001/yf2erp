import requests
import GetSetting


def getXML(fileXML):
    """
    获取xml文本
    :param order: 订单号
    :return:
    """
    f = open('./documents/' + fileXML, encoding='utf-8')
    dataXML = f.read()
    f.close()
    return dataXML


def sendERP(order):
    """
    发送订单的xml数据到erp接口
    :param order:订单号
    :return:
    """
    url = GetSetting.get_setting('user', 'url')

    dataXML = getXML(order)

    headers = {"Content-Type": "text/xml; charset=UTF-8", 'Connection': 'close'}

    response = requests.post(url, data=dataXML, headers=headers)

    # print(response.text)

    # 如果是json文件可以直接显示
    # print(response.json())
    return response.text


if __name__ == '__main__':
    url = GetSetting.get_setting("user", "url")
    print(url)
    print(getXML('成都04-2019-5-321B-05主卧衣柜.xml'))
