import os
import csv

class EntityDictionary:
    # col1 = TABLE_CATALOG, col2 = TABLE_SCHEMA, col3 = TABLE_NAME, col4 = COLUMN_NAME, col4= LOGICAL_NAME
    FILE_PATH = os.path.join('file', 'import', '')
    IMPORT_FILE_NAME = 'a5m2_COLUMNS'
    COLUMN_ENTITY_NAME = 'COLUMN_NAME'
    COLUMN_ENTITY_JP_NAME = 'LOGICAL_NAME'

    def __init__(self):
        return
    @classmethod
    def importER(cls):
        print("hi")

        entity_dictionary_file = open(cls.FILE_PATH + cls.IMPORT_FILE_NAME + '.csv')
        csv_file_obj = csv.DictReader(entity_dictionary_file)

        e_dictionary = {}

        for row in csv_file_obj:
            key = row[cls.COLUMN_ENTITY_JP_NAME]
            value = row[cls.COLUMN_ENTITY_NAME]
            e_dictionary[key] = value

        entity_dictionary_file.close()

        return e_dictionary
