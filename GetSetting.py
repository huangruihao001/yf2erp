import configparser

def get_setting(section, name):
    """
    获取setting.ini中的配置
    :param section:节
    :param name:键
    :return:值
    """
    config = configparser.ConfigParser()
    config.read('./setting.ini', encoding='utf-8')
    value = config.get(section, name)
    return value