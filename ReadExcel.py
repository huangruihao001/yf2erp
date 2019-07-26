import xlrd

class ReadExcel():


    def __init__(self, workbook_path, sheet_name):
        self.workbook_path = workbook_path # excel路径
        self.sheet_name = sheet_name # 表格名称
        self.xml_workbook = xlrd.open_workbook(self.workbook_path) # 创建表格对象
        self.xml_sheet = self.xml_workbook.sheet_by_name(self.sheet_name) # 创建工作簿对象
        self.order = str(self.xml_sheet.cell_value(1, 0)) # 主订单号
        self.Eorder = str(self.xml_sheet.cell_value(1, 0)) # 子订单号
        self.first_row = self.date_row(1) # 第一行数据列表
        self.max_row = self.xml_sheet.nrows # 最大行数
        self.max_column = self.xml_sheet.ncols # 最大列数


    def date_row(self, row):# 某一行的数据列表
        date_row_list = []
        for i in self.xml_sheet.row(row-1):
            date_row_list.append(str(i.value))
        return date_row_list


if __name__ == '__main__':
    a = ReadExcel("./documents/圣萝莎erp输出输出参考.xls", "ERP表")
    print(a.Eorder)
    print(a.first_row)
    print(a.max_row)
    print(a.max_column)