import os
import csv

# utf8で読み込む
# col1 = TABLE_CATALOG, col2 = TABLE_SCHEMA, col3 = TABLE_NAME, col4 = COLUMN_NAME, col4= LOGICAL_NAME
FILE_PATH = os.path.join('file', 'import', '')
IMPORT_FILE_NAME = 'a5m2_COLUMNS'
COLUMN_ENTITY_NAME = 'COLUMN_NAME'
COLUMN_ENTITY_JP_NAME = 'LOGICAL_NAME'

"""
A5ERのCSV Export機能を使用し、出力したCSVを読込み
key:論理名、value:物理名のdictionaryを作成する
"""
def importDictionary():

    entity_dictionary_file = open(FILE_PATH + IMPORT_FILE_NAME + '.csv', encoding="utf_8")
    csv_file_obj = csv.DictReader(entity_dictionary_file)

    e_dictionary = {}

    for row in csv_file_obj:
        key = row[COLUMN_ENTITY_JP_NAME]
        value = row[COLUMN_ENTITY_NAME]
        e_dictionary[key] = value

    entity_dictionary_file.close()

    return e_dictionary
