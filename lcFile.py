import re

class LCFile:

    def __init__(self):
        return

    @classmethod
    def out(cls, t_sheet, e_dictionary):

        for i in range(11, 100):  # lengthはあとから

            jp_name = t_sheet.cell(row=i, column=4).value
            attr_mode = t_sheet.cell(row=i, column=8).value
            str_position = str(t_sheet.cell(row=i, column=11).value)
            end_position = str(t_sheet.cell(row=i, column=12).value)

            # TODO Noneになったら終了、なんか式間違っているらしい
            if jp_name == None:
                break

            en_name = e_dictionary.get(jp_name, 'NonMatchMethodName')
            method_name = re.sub("_(.)", lambda x: x.group(1).upper(), en_name)

            print("/** " + jp_name + " */")
            print("@InputFixedLengthColumn(start = " + str_position + ", end = " + end_position + ")")
            print("public String " + method_name + ";")
