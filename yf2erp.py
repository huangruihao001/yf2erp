import os
import CreatXml
import SendERP

def creatXML():
    # 批量生成xml文件
    file_list = os.listdir('./documents')
    print(file_list)
    for file in file_list:
        if '.xls' in file:
            fileXML = CreatXml.CreatXml("./documents/" + file, "ERP表")
            fileXML.writeXML()
            del fileXML


def uploadXML():
    # 批量上传xml文件
    xml_list = os.listdir('./documents')
    print(xml_list)
    for file in xml_list:
        if '.xml' in file:
            print(SendERP.getXML(file))
            os.remove("./documents/" + file) # 删除xml缓存文件


if __name__ == '__main__':
    creatXML()
    uploadXML()

