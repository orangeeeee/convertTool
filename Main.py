import os

import openpyxl

from entityDictionary import EntityDictionary
from cl import ClFile

FILE_PATH = os.path.join('file', 'import', '')
file_list = os.listdir(FILE_PATH)
menu_list_str = "読込むファイル番号を入力してください" + os.linesep

for i in range(len(file_list)):
    menu_list_str += str(i) + ":" + file_list[i] + os.linesep


# In[1]:\
print(menu_list_str)
select_number = input()

e_dictionary = EntityDictionary.importER()

# "file\\import\\"
INPUT_FILE_NAME = file_list[int(select_number)]

# data_only=Trueにする？
wb = openpyxl.load_workbook(FILE_PATH + INPUT_FILE_NAME, data_only=True)

firstSheetName = wb.sheetnames[0]

t_sheet = wb[firstSheetName]

ClFile.out(t_sheet, e_dictionary)

print("終了しますか？")
input()