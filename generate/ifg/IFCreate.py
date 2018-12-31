import re
from distutils.util import strtobool

from generate.template.IFTemplete import IFTemplate


class IFCreate:

    def __init__(self):
        return

    @classmethod
    def out(cls, t_sheet, e_dictionary, generate_target):

        clazzName = cls.convertNumericToStr(t_sheet.cell(row=1, column=2).value)

        output_str = IFTemplate.interface_template.format(clazzName=clazzName)

        for i in range(3, 100):  # TODO lengthはあとから

            jp_name = t_sheet.cell(row=i, column=1).value

            if jp_name is None:
                break

            isOpt = strtobool(t_sheet.cell(row=i, column=2).value)
            _type = t_sheet.cell(row=i, column=3).value  # TODO 辞書からとるべき

            en_name = e_dictionary.get(jp_name, 'NonMatchMethodName')
            # toCamelCase
            method_name = re.sub("_(.)", lambda x: x.group(1).upper(), en_name)

            if generate_target == '1' or generate_target == '2':
                # Optional用のテンプレートと分けて作成する
                if isOpt:
                    output_str += IFTemplate.opt_getter_template.format(
                        jp_name=jp_name, type=_type, clazzName=clazzName, method_name=method_name)
                else:
                    output_str += IFTemplate.getter_template.format(
                        jp_name=jp_name, type=_type, clazzName=clazzName, method_name=method_name)

            if generate_target == '1' or generate_target == '3':
                # Optional用のテンプレートと分けて作成する
                if isOpt:
                    output_str += IFTemplate.opt_setter_template.format(
                        jp_name=jp_name, type=_type, clazzName=clazzName, method_name=method_name)
                else:
                    output_str += IFTemplate.setter_template.format(
                        jp_name=jp_name, type=_type, clazzName=clazzName, method_name=method_name)

        output_str += '}'

        return output_str

    @classmethod
    def convertNumericToStr(cls, val):
        result = ""
        if isinstance(val, float):
            result = str(int(val))
        else:
            result = str(val)
        return result
