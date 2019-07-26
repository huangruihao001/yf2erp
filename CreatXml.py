import time
from xml.dom import minidom
from ReadExcel import *


class CreatXml():
    """
    根据xls创建对应的xml文件
    """

    def __init__(self, workbook_path, sheet_name):
        self.workbook_path = workbook_path  # xls表格名称
        self.sheet_name = sheet_name  # xls工作簿名称
        self.excelOBJ = ReadExcel(self.workbook_path, self.sheet_name)  # 创建读取xls对象
        self.dom = minidom.Document()  # 创建根节点。每次都要用DOM对象来创建任何节点。
        self.Order_node = self.dom.createElement('Order')  # 创建主订单号标签
        self.EOrder_node = self.dom.createElement('EOrder')  # 创建子订单号标签
        self.date_row = self.excelOBJ.max_row  # xls最大行数
        self.date_column = self.excelOBJ.max_column  # xls最列行数

    def creat_Order(self):
        """
        创建主订单号和子订单号标签
        :param OrderID: 主订单号
        :param EOrderID: 子订单号
        :return:
        """
        self.Order_node.setAttribute('ID', self.excelOBJ.order)
        self.Order_node.setAttribute('create_time', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        self.Order_node.setAttribute('Remark', '主订单号')
        # 3.用DOM对象添加根节点
        self.dom.appendChild(self.Order_node)

        self.Order_node.appendChild(self.EOrder_node)
        self.EOrder_node.setAttribute('ID', self.excelOBJ.Eorder)
        self.EOrder_node.setAttribute('Remark', '子订单号')

    def cabinet_date(self, date_row, date_column, code_node):
        """
        生成板件详细信息的标签
        :param date_row:
        :param date_column:
        :param code_node:
        :return:
        """
        label = str(self.excelOBJ.first_row[date_column]).replace('(', '_').replace(')', '')
        i_node = self.dom.createElement(label)
        code_node.appendChild(i_node)
        name_text = self.dom.createTextNode(str(self.excelOBJ.date_row(date_row)[date_column]))
        i_node.appendChild(name_text)

    def board_code(self, date_row):
        """
        生成板件编号标签页
        :param date_row:
        :return:
        """
        code_node = self.dom.createElement('Product')
        code_node.setAttribute('CodeID', str(self.excelOBJ.date_row(date_row)[4]))
        code_node.setAttribute('MaterialID', str(self.excelOBJ.date_row(date_row)[6]))
        self.EOrder_node.appendChild(code_node)

        # 生成板件详细信息的标签
        for i in range(1, self.date_column):  # 去除空标签
            if self.excelOBJ.date_row(date_row)[i] == '':
                continue
            self.cabinet_date(date_row, i, code_node)

    def board_code_all(self, date_row):
        """
        生成所有板件详细信息的标签
        :param date_row:
        :return:
        """
        for i in range(2, date_row + 1):  # 去除空行
            if self.excelOBJ.date_row(i)[0] == '':
                continue
            self.board_code(i)

    def writeXML(self):
        """
        按XML标准格式写入并保存
        :param Order: 订单号作为保存XML的文件名
        :return:
        """
        self.creat_Order()  # 创建主订单号和子订单号标签
        self.board_code_all(self.excelOBJ.max_row)  # 创建板件详情xml
        try:
            with open('./documents/' + self.excelOBJ.order + '.xml', 'w', encoding='UTF-8') as fh:
                # 4.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
                # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
                self.dom.writexml(fh, indent='', addindent='\t', newl='\n', encoding='UTF-8')
                print('写入xml OK!')
        except Exception as err:
            print('错误信息：{0}'.format(err))


if __name__ == '__main__':
    a = CreatXml("./documents/圣萝莎erp输出输出参考.xls", "ERP表")
    a.writeXML()
    print(a.dom)
    print(a.dom.childNodes)
