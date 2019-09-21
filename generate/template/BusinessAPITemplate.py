class BusinessAPITemplate:

    def __init__(self):
        return

    imple_template = '''package jp.co.happinet.commerce.app.api.business.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.api.dto.{package}.DerivedHeader;
import jp.co.happinet.commerce.app.api.dto.{package}.HeaderDTO;
import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name};

import java.util.List;

public interface {class_name}BusinessAPI {{

    @NotNull DerivedHeader deriveAndValidateHeader(@NotNull final HeaderDTO<?, ?> dto);

    @NotNull DerivedHeader deriveAndValidateLines(@NotNull final HeaderDTO<?, ?> dto);

    @NotNull String register(@NotNull final HeaderDTO<?, ?> dto);

    void cancel(@NotNull final List<String> number);

    @NotNull ProductReplacementDirectionHeader get(@NotNull final String number);
}}


'''

    clazz_template = '''package jp.co.happinet.commerce.app.api.business.{package}.impl;

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.generated.entity.{domain_package}.*;

import jp.co.happinet.commerce.app.api.business.helper.CancelHelperService;
import jp.co.happinet.commerce.app.api.business.inventory.EndingInventoryBusinessAPI;
import jp.co.happinet.commerce.app.api.business.inventory.EndingInventoryExistence;
import jp.co.happinet.commerce.app.api.business.inventory.InventoryBusinessAPI;
import jp.co.happinet.commerce.app.api.business.inventory.InventoryReceiveAndSendBusinessAPI;
import jp.co.happinet.commerce.app.api.business.{package}.{class_name}BusinessAPI;
import jp.co.happinet.commerce.app.api.business.{package}.{class_name}HeaderBusinessAPI;
import jp.co.happinet.commerce.app.api.dto.{package}.DerivedHeader;
import jp.co.happinet.commerce.app.api.dto.{package}.HeaderDTO;
import jp.co.happinet.commerce.app.api.validation.{package}.{class_name}HeaderValidationAPI;
import jp.co.happinet.commerce.app.api.validation.{package}.{class_name}InventoryValidationAPI;
import jp.co.happinet.commerce.app.api.validation.{package}.{class_name}LineValidationAPI;
import jp.co.happinet.commerce.app.domain.common.Sign;
import jp.co.happinet.commerce.app.domain.common.inventory.TransferInventoryManagementContext;
import jp.co.happinet.commerce.app.domain.common.inventory.context.InventoryManagementContext;
import jp.co.happinet.commerce.app.domain.common.inventory.context.InventoryQuantityContext;
import jp.co.happinet.commerce.app.domain.common.inventory.context.TransferInventoryContextOperand;
import jp.co.happinet.commerce.app.domain.inventory.Inventories;
import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name};
import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name}Header;
import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name}Line;
import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name}s;
import jp.co.happinet.commerce.app.domain.{domain_package}.ProductReplacementFromAchievementHeader;
import jp.co.happinet.commerce.app.domain.{domain_package}.ProductReplacementToAchievementHeader;
import jp.co.happinet.commerce.fw.utils.intension.BusinessLogic;

import java.util.List;
import javax.annotation.Resource;

import org.springframework.stereotype.Service;

import static jp.co.happinet.commerce.fw.entity.persistence.DAO.*;
import static jp.co.happinet.commerce.fw.utils.MacroLike.*;


@Service
public class {class_name}BusinessAPIImpl
    implements {class_name}BusinessAPI {{

    @Resource
    {class_name}HeaderBusinessAPI headerBusinessAPI;

    @Resource
    EndingInventoryBusinessAPI endingInventoryBusinessAPI;

    @Resource
    {class_name}HeaderValidationAPI headerValidationAPI;

    @Resource
    {class_name}LineValidationAPI lineValidationAPI;


    @Resource
    private {class_name}s {class_name}s;


    @Override
    public @NotNull DerivedHeader deriveAndValidateHeader(@NotNull final HeaderDTO<?, ?> dto) {{
        return this.headerBusinessAPI.deriveAndValidateHeader(dto);
    }}

    @Override
    public @NotNull DerivedHeader deriveAndValidateLines(@NotNull final HeaderDTO<?, ?> dto) {{

        final var derived = this.headerBusinessAPI.deriveAndValidateLines(dto);

        this.deriveAndValidateInventoryContext(derived.fromHeader(), derived.toHeader());

        return derived;
    }}

    @Override
    public @NotNull String register(@NotNull final HeaderDTO<?, ?> dto) {{

        this.beforeValidate(dto);

        final var derive = this.headerBusinessAPI.derive(dto);

        this.afterValidation(derive);

        final var merged = this.mergeAndFetch(derive.{class_name}());

        return FIXME();
    }}

    private void beforeValidate(@NotNull final HeaderDTO<?, ?> dto) {{

        this.headerValidationAPI.beforeValidate(dto);

        this.lineValidationAPI.beforeValidate(dto);
    }}

    private void afterValidation(@NotNull final DerivedHeader derived) {{

        this.headerValidationAPI.afterValidate(derived);

        this.lineValidationAPI.afterValidate(derived);
    }}

    @Override
    public void cancel(@NotNull final List<String> numbers) {{
        FIXME();
    }}

    @Override
    public @NotNull {class_name} get(@NotNull final String number) {{

        return FIXME("this.{class_name}s.findOrDeath(number);");
    }}

    private @NotNull ProductReplacementDirectionHeader mergeAndFetch(
        @NotNull final ProductReplacementDirectionHeader header) {{
            
            //TODO complete Number
        
        return FIXME("this.{class_name}s.mergeAndFetch({class_name})");
    }}
}}


'''
