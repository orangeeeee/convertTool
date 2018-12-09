import os

import openpyxl
import pyperclip as pyperclip

from generate.clFile import CLFile
from dictionary.entityDictionary import EntityDictionary
from generate.lcFile import LCFile

FILE_PATH = os.path.join('file', 'import', '')
file_list = os.listdir(FILE_PATH)
menu_list_str = "読込むファイル番号を入力してください" + os.linesep

for i in range(len(file_list)):
    menu_list_str += str(i + 1) + ":" + file_list[i] + os.linesep

# In[1]:\
print(menu_list_str)
select_number = input()

print("ファイルタイプを選択してください。" + os.linesep + "1 : LC" + os.linesep + "2 : CL")
import_file_type = input()

e_dictionary = EntityDictionary.importER()

# "file\\import\\"
INPUT_FILE_NAME = file_list[int(select_number) - 1]

# data_only=Trueにする？
wb = openpyxl.load_workbook(FILE_PATH + INPUT_FILE_NAME, data_only=True)

firstSheetName = wb.sheetnames[0]

t_sheet = wb[firstSheetName]

clip_board_str = ""

if import_file_type == '1':
    clip_board_str = LCFile.out(t_sheet, e_dictionary)
else:
    clip_board_str = CLFile.out(t_sheet, e_dictionary)

pyperclip.copy(clip_board_str)

print("クリップボードにコピーしました。")
input()
