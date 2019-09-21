import os

import openpyxl
import pyperclip as pyperclip

from dictionary.additionalDictionary import AdditionalDictionary
from dictionary.entityDictionary import EntityDictionary
from generate.ifg.IFCreate import IFCreate

print("生成対象を選択してください。" + os.linesep
      + "1 : Setter and Getter" + os.linesep
      + "2 : Getter" + os.linesep
      + "3 : Setter")

generate_target = input()

e_dictionary = EntityDictionary.importER()

additional_dictionary = AdditionalDictionary.importDict2(e_dictionary)
e_dictionary.update(additional_dictionary)

FILE_PATH = os.path.join('file', 'import', '')

wb = openpyxl.load_workbook(FILE_PATH + 'generateIFImport.xlsx', data_only=True)

firstSheetName = wb.sheetnames[0]

t_sheet = wb[firstSheetName]

clip_board_str = IFCreate.out(t_sheet, e_dictionary, generate_target)

pyperclip.copy(clip_board_str)

print("クリップボードにコピーしました。")
input()
