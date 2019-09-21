import os

from generate.template.EndpointTemplate import EndpointTemplate
from generate.template.BusinessAPITemplate import BusinessAPITemplate
from generate.template.ValidationAPITemplate import ValidationAPITemplate
from generate.template.DtoTemplate import DtoTemplate

_package = 'product_replacement.work'
_domain_package = 'product_replacement_direction'
clazzName = 'ProductReplacementWork'

base_dir = 'C:/Users/kurata/IdeaProjects/commerce/'
endpoint_dir = 'app-endpoint/src/main/java/jp/co/happinet/commerce/app/endpoint/'
biz_dir = "app-api/src/main/java/jp/co/happinet/commerce/app/api/business/"
validate_biz_dir = "app-api/src/main/java/jp/co/happinet/commerce/app/api/validation/"
create_dir = 'product_replacement/work/'
imple_dir = 'impl/'
dto_interface_dir = 'app-api/src/main/java/jp/co/happinet/commerce/app/api/dto/'

endpoint_target_dir = base_dir + endpoint_dir + create_dir

biz_target_dir = base_dir + biz_dir + create_dir
biz_impl_target_dir = biz_target_dir + imple_dir

validate_biz_target_dir = base_dir + validate_biz_dir + create_dir
validate_biz_imple_target_dir = base_dir + validate_biz_dir + create_dir + imple_dir

dto_interface_target_dir = base_dir + dto_interface_dir + create_dir

# TODO Endpoint  はじめにディレクトリ作成
os.makedirs(endpoint_target_dir, exist_ok=True)
os.makedirs(biz_target_dir, exist_ok=True)
os.makedirs(biz_impl_target_dir, exist_ok=True)
os.makedirs(dto_interface_target_dir, exist_ok=True)
os.makedirs(validate_biz_target_dir, exist_ok=True)
os.makedirs(validate_biz_imple_target_dir, exist_ok=True)

output_endpoint_str = EndpointTemplate.clazz_template.format(class_name=clazzName, package=_package)

output_abstract_endpoint_str = EndpointTemplate.abstract_clazz_template.format(class_name=clazzName, package=_package)

f = open(endpoint_target_dir + clazzName + 'Endpoint.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(output_endpoint_str)  # 文字列を記載する
f.close()  # ファイルを閉じる

f1 = open(endpoint_target_dir + 'Abstract' + clazzName + 'Endpoint.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f1.write(output_abstract_endpoint_str)  # 文字列を記載する
f1.close()  # ファイルを閉じる

# TODO BusinessAPI

output_biz_if_str = BusinessAPITemplate.imple_template.format(class_name=clazzName, package=_package,
                                                              domain_package=_domain_package)
output_biz_str = BusinessAPITemplate.clazz_template.format(class_name=clazzName, package=_package,
                                                           domain_package=_domain_package)
f3 = open(biz_impl_target_dir + clazzName + 'BusinessAPIImpl.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f3.write(output_biz_str)  # 文字列を記載する
f3.close()  # ファイルを閉じる

f4 = open(biz_target_dir + clazzName + 'BusinessAPI.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f4.write(output_biz_if_str)  # 文字列を記載する
f4.close()

# dto_interface_target_dir

output_line_dto_str = DtoTemplate.line_template.format(class_name=clazzName, package=_package,
                                                       domain_package=_domain_package)
f = open(dto_interface_target_dir + 'LineDTO.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(output_line_dto_str)  # 文字列を記載する
f.close()  # ファイルを閉じる

output_header_dto_str = DtoTemplate.header_template.format(class_name=clazzName, package=_package,
                                                           domain_package=_domain_package)
f5 = open(dto_interface_target_dir + 'HeaderDTO.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f5.write(output_header_dto_str)  # 文字列を記載する
f5.close()

derived_toLine_template_str = DtoTemplate.derived_toLine_template.format(class_name=clazzName, package=_package,
                                                                         domain_package=_domain_package)
f6 = open(dto_interface_target_dir + 'DerivedToLine.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f6.write(derived_toLine_template_str)  # 文字列を記載する
f6.close()  # ファイルを閉じる

derived_fromLine_template_str = DtoTemplate.derived_fromLine_template.format(class_name=clazzName, package=_package,
                                                                             domain_package=_domain_package)
f = open(dto_interface_target_dir + 'DerivedFromLine.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(derived_fromLine_template_str)  # 文字列を記載する
f.close()  # ファイルを閉じる

derived_line_template_str = DtoTemplate.derived_line_template.format(class_name=clazzName, package=_package,
                                                                     domain_package=_domain_package)
f = open(dto_interface_target_dir + 'DerivedLine.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(derived_line_template_str)  # 文字列を記載する
f.close()  # ファイルを閉じる

derived_header_template_str = DtoTemplate.derived_header_template.format(class_name=clazzName, package=_package,
                                                                         domain_package=_domain_package)
f = open(dto_interface_target_dir + 'DerivedHeader.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(derived_header_template_str)  # 文字列を記載する
f.close()  # ファイルを閉じる

# TODO バリデーションAPI
header_interface_template_str = ValidationAPITemplate.header_interface_template.format(class_name=clazzName,
                                                                                       package=_package,
                                                                                       domain_package=_domain_package)
f = open(validate_biz_target_dir + clazzName + 'HeaderValidationAPI.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(header_interface_template_str)  # 文字列を記載する
f.close()  # ファイル

header_clazz_template_str = ValidationAPITemplate.header_clazz_template.format(class_name=clazzName, package=_package,
                                                                               domain_package=_domain_package)
f = open(validate_biz_imple_target_dir + clazzName + 'HeaderValidationAPIImpl.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(header_clazz_template_str)  # 文字列を記載する
f.close()  # ファイル

# TODO Line　バリデーションAPI
line_interface_template_str = ValidationAPITemplate.line_interface_template.format(class_name=clazzName,
                                                                                   package=_package,
                                                                                   domain_package=_domain_package)
f = open(validate_biz_target_dir + clazzName + 'LineValidationAPI.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(header_interface_template_str)  # 文字列を記載する
f.close()  # ファイル

line_clazz_template_str = ValidationAPITemplate.line_clazz_template.format(class_name=clazzName, package=_package,
                                                                           domain_package=_domain_package)
f = open(validate_biz_imple_target_dir + clazzName + 'LineValidationAPIImpl.java', 'w')  # ファイルを開く(該当ファイルがなければ新規作成)
f.write(line_clazz_template_str)  # 文字列を記載する
f.close()  # ファイル
