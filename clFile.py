import re


class CLFile:

    def __init__(self):
        return

    # /** Ｈ汎用文字8 */
    # @OutputFixedColumn(byteSize = 40, mode = Mode.A)

    @classmethod
    def out(cls, t_sheet, e_dictionary):

        for i in range(11, 1000):  # lengthはあとから

            jp_name = t_sheet.cell(row=i, column=3).value
            attr_mode = t_sheet.cell(row=i, column=12).value
            byteSize = str(t_sheet.cell(row=i, column=14).value)

            # TODO Noneになったら終了、なんか式間違っているらしい
            if jp_name is None:
                continue

            en_name = e_dictionary.get(jp_name, 'NonMatchMethodName')
            method_name = re.sub("_(.)", lambda x: x.group(1).upper(), en_name)

            print("/** " + jp_name + " */")
            print("@OutputFixedColumn(byteSize = " + str(byteSize) + ", mode = Mode." + attr_mode + ")")
            print("public String " + method_name + ";")
