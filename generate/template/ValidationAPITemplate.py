class ValidationAPITemplate:

    def __init__(self):
        return

    header_interface_template = '''package jp.co.happinet.commerce.app.api.validation.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.api.dto.{package}.DerivedHeader;
import jp.co.happinet.commerce.app.api.dto.{package}.HeaderDTO;
import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name};


public interface {class_name}HeaderValidationAPI {{

    void beforeValidate(@NotNull final HeaderDTO<?, ?> dto);

    void afterValidate(@NotNull final DerivedHeader derived);

    void cancelable(@NotNull final ProductReplacementDirectionHeader header);
}}

    '''

    header_clazz_template = '''package jp.co.happinet.commerce.app.api.validation.{package}.impl;

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.api.dto.{package}.DerivedHeader;
import jp.co.happinet.commerce.app.api.dto.{package}.HeaderDTO;
import jp.co.happinet.commerce.app.api.validation.BusinessMonthValidationAPI;
import jp.co.happinet.commerce.app.api.validation.WarehouseValidationAPI;
import jp.co.happinet.commerce.app.api.validation.organization.SectionValidationAPI;
import jp.co.happinet.commerce.app.api.validation.{package}.{class_name}HeaderValidationAPI;
import jp.co.happinet.commerce.app.domain.business_control.BusinessDates;
import jp.co.happinet.commerce.app.domain.organization.Sections;
import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name};
import jp.co.happinet.commerce.app.domain.warehouse.Warehouses;
import jp.co.happinet.commerce.fw.utils.validation.ValidationResult;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import static jp.co.happinet.commerce.fw.utils.MacroLike.*;


@Service
public class {class_name}HeaderValidationAPIImpl
    implements {class_name}HeaderValidationAPI {{

    @Resource
    private WarehouseValidationAPI warehouseValidationAPI;

    @Resource
    private SectionValidationAPI sectionValidationAPI;

    @Resource
    private BusinessMonthValidationAPI businessMonthValidationAPI;

    @Resource
    private Warehouses warehouses;

    @Resource
    private Sections sections;

    @Resource
    private BusinessDates bizDates;

    @Override
    public void beforeValidate(@NotNull final HeaderDTO<?, ?> dto) {{

        new ValidationResult()//
            .raiseOnFail();
        FIXME();
    }}

    @Override
    public void afterValidate(@NotNull final DerivedHeader derived) {{

        FIXME();
    }}

    @Override
    public void cancelable(@NotNull final ProductReplacementDirectionHeader header) {{

        FIXME();
    }}
}}


    '''

    line_interface_template = '''package jp.co.happinet.commerce.app.api.validation.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.api.dto.{package}.DerivedHeader;
import jp.co.happinet.commerce.app.api.dto.{package}.HeaderDTO;


public interface {class_name}LineValidationAPI {{

    void beforeValidate(@NotNull final HeaderDTO<?, ?> dto);

    void afterValidate(@NotNull final DerivedHeader derived);
}}


    '''

    line_clazz_template = '''package jp.co.happinet.commerce.app.api.validation.{package}.impl;

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.api.dto.{package}.DerivedHeader;
import jp.co.happinet.commerce.app.api.dto.{package}.HeaderDTO;
import jp.co.happinet.commerce.app.api.validation.product.ProductValidationAPI;
import jp.co.happinet.commerce.app.api.validation.product.UnitValidationAPI;
import jp.co.happinet.commerce.app.api.validation.{package}.{class_name}LineValidationAPI;
import jp.co.happinet.commerce.app.domain.product.Products;
import jp.co.happinet.commerce.fw.utils.intension.BusinessLogic;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import static jp.co.happinet.commerce.fw.utils.MacroLike.*;


@Service
public class {class_name}LineValidationAPIImpl
    implements {class_name}LineValidationAPI {{

    @Resource
    private Products products;

    @Resource
    private ProductValidationAPI productValidationAPI;

    @Resource
    private UnitValidationAPI unitValidationAPI;

    @Override
    @BusinessLogic(id = "BL-P000784")
    public void beforeValidate(@NotNull final HeaderDTO<?, ?> dto) {{

        FIXME();
    }}

    @Override
    public void afterValidate(@NotNull final DerivedHeader derived) {{

        FIXME();
    }}
}}


    '''
