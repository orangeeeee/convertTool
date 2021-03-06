import re

from generate.template.lcTemplate import LCTemplate


class LCFile:

    def __init__(self):
        return

    @classmethod
    def out(cls, t_sheet, e_dictionary):

        output_str = ""

        for i in range(11, 1000):  # TODO lengthはあとから

            jp_name = t_sheet.cell(row=i, column=4).value

            str_position = cls.convertNumericToStr(t_sheet.cell(row=i, column=11).value)
            end_position = cls.convertNumericToStr(t_sheet.cell(row=i, column=12).value)

            if jp_name is None:
                break

            en_name = e_dictionary.get(jp_name, 'NonMatchMethodName')
            method_name = re.sub("_(.)", lambda x: x.group(1).upper(), en_name)

            output_str += LCTemplate.method_template.format(
                jp_name=jp_name, str_position=str_position, end_position=end_position,
                method_name=method_name)

        return output_str

    @classmethod
    def convertNumericToStr(cls, val):
        result = ""
        if isinstance(val, float):
            result = str(int(val))
        else:
            result = str(val)
        return result
