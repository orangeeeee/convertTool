import os
import re


class LCFile:

    def __init__(self):
        return

    method_template = '''/** {jp_name}  */
    @InputFixedLengthColumn(start = {str_position} , end = {end_position} )
    public String {method_name};
    
    '''

    @classmethod
    def out(cls, t_sheet, e_dictionary):

        output_str = ""

        for i in range(11, 1000):  # lengthはあとから

            jp_name = t_sheet.cell(row=i, column=4).value
            str_position = str(t_sheet.cell(row=i, column=11).value)
            end_position = str(t_sheet.cell(row=i, column=12).value)

            if jp_name is None:
                break

            en_name = e_dictionary.get(jp_name, 'NonMatchMethodName')
            method_name = re.sub("_(.)", lambda x: x.group(1).upper(), en_name)

            output_str += cls.method_template.format(
                jp_name=jp_name, str_position=str_position, end_position=end_position,
                method_name=method_name)

        return output_str
