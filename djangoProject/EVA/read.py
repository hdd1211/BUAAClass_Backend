import pandas as pd
from openpyxl import load_workbook
from .models import Course


def get_xlsx():
    workbook = load_workbook(filename='path/to/your/file.xlsx')

    for worksheet in workbook.worksheets:
        for row in worksheet.iter_rows(values_only=True):
            1
# A 名称  B 本科生/研究生 C 校区 D 开课学院 E 课程类别  F老师姓名 G课程性质（必修等）H节次 I 课程代码
# J选课人数 K 老师职称 L 上课时间 M 上课地点
#
