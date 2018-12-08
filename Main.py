import openpyxl
import pprint
import os

print(os.getcwd())
FILE_PATH = os.path.join('file', 'import', '')
#"file\\import\\"
INPUT_FILE_NAME = "出荷指示取消IF.xlsx"

# data_only=Trueにする？
wb = openpyxl.load_workbook(FILE_PATH + INPUT_FILE_NAME)

firstSheetName = wb.sheetnames[0]

t_sheet = wb[firstSheetName]
g = t_sheet.iter_rows(min_row=2, max_row=4, min_col=1, max_col=3)
pprint.pprint(list(g))


# ここまでは共通


#for cell_obj in list(t_sheet.columns)[3]:
#    print(cell_obj.value)
