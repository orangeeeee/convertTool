import os
import re


class LCFile:

    def __init__(self):
        return

    @classmethod
    def out(cls, t_sheet, e_dictionary):

        output_str = ""

        for i in range(11, 100):  # lengthはあとから

            jp_name = t_sheet.cell(row=i, column=4).value
            str_position = str(t_sheet.cell(row=i, column=11).value)
            end_position = str(t_sheet.cell(row=i, column=12).value)

            if jp_name is None:
                break

            en_name = e_dictionary.get(jp_name, 'NonMatchMethodName')
            method_name = re.sub("_(.)", lambda x: x.group(1).upper(), en_name)

            output_str += "/** " + jp_name + " */" + os.linesep
            output_str += "@InputFixedLengthColumn(start = " + str_position + ", end = " + end_position + ")" + os.linesep
            output_str += "public String " + method_name + ";" + os.linesep

        return output_str
