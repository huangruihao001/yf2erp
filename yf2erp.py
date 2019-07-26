import os
import CreatXml
import SendERP

file_list = os.listdir('./documents')
print(file_list)
# 批量生成xml文件
for file in file_list:
    if '.xls' in file:
        fileXML = CreatXml.CreatXml("./documents/" + file, "ERP表")
        fileXML.writeXML()
        del fileXML

xml_list = os.listdir('./documents')
print(xml_list)
# 批量上传xml文件
for file in xml_list:
    if '.xml' in file:
        print(SendERP.getXML(file))
        