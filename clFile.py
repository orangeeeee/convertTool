import os
import re


class CLFile:

    def __init__(self):
        return

    method_template = '''/** " {jp_name}  */
    @OutputFixedColumn(byteSize = {byteSize}, mode = Mode.{attr_mode})
    public String {method_name};

    '''

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

            output_str += cls.method_template.format(
                jp_name=jp_name, byteSize=byteSize, attr_mode=attr_mode,
                method_name=method_name)

        return output_str
