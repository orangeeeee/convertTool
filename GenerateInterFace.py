import os

import openpyxl
import pyperclip as pyperclip

from dictionary.entityDictionary import EntityDictionary
from generate.ifg.IFCreate import IFCreate

e_dictionary = EntityDictionary.importER()

FILE_PATH = os.path.join('file', 'import', '')

wb = openpyxl.load_workbook(FILE_PATH + 'generateIFImport.xlsx', data_only=True)

firstSheetName = wb.sheetnames[0]

t_sheet = wb[firstSheetName]


clip_board_str = IFCreate.out(t_sheet, e_dictionary)

pyperclip.copy(clip_board_str)

print("クリップボードにコピーしました。")
input()
