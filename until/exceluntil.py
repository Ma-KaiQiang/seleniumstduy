# coding=utf-8
import sys

sys.path.append(r"D:\student\pycharm\项目\seleniumstduy")
import xlrd
from xlutils.copy import copy
import os
import time


class ExcelUntil:
    def __init__(self, sheetName, excelFile_path=None):
        if excelFile_path == None:
            self.excelFile_path = os.path.join(os.path.dirname(__file__) + '/../config/casedata.xls')
        else:
            self.excelFile_path = excelFile_path
        self.data = xlrd.open_workbook(self.excelFile_path)
        self.sheetName = sheetName
        self.table = self.data.sheet_by_name(self.sheetName)
        self.excelList = []

    # 从excel中获取数据
    def get_lines(self):
        rowNum = self.table.nrows
        if rowNum >= 1:
            return rowNum
        else:
            return None

    def next(self):
        if self.get_lines() >= 1:
            # 使用列表推导式
            self.excelList = [self.table.row_values(i) for i in range(5)]
            return self.excelList
        else:
            print('excel表中没有数据')
            return None

    # 获取单元格数据
    def get_cell_value(self, row, col):
        if self.get_lines() >= row:
            cell_data = self.table.cell_value(row, col)
            return cell_data
        else:
            return None

    # 向excel中写入数据
    def write_value(self, row, value):
        write_data = copy(self.data)
        write_data.get_sheet(0).write(row, 7, value)
        write_data.save(self.excelFile_path)
        time.sleep(1)

# if __name__ == '__main__' :
#     e=ExcelUntil('Sheet1')
#     # v=e.get_cell_value(1,1)
#     print(e.get_lines())
#     v=e.next()
#     print(v)
