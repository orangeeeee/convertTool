import os
import re


class CLFile:

    def __init__(self):
        return

    @classmethod
    def out(cls, t_sheet, e_dictionary):

        output_str = ""

        for i in range(11, 1000):  # lengthはあとから

            jp_name = t_sheet.cell(row=i, column=3).value
            attr_mode = t_sheet.cell(row=i, column=12).value
            byteSize = str(t_sheet.cell(row=i, column=14).value)

            if jp_name is None:
                continue

            en_name = e_dictionary.get(jp_name, 'NonMatchMethodName')
            method_name = re.sub("_(.)", lambda x: x.group(1).upper(), en_name)

            output_str += "/** " + jp_name + " */" + os.linesep
            output_str += "@OutputFixedColumn(byteSize = " + str(
                byteSize) + ", mode = Mode." + attr_mode + ")" + os.linesep
            output_str += "public String " + method_name + ";" + os.linesep

        return output_str
