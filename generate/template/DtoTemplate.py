class DtoTemplate:

    def __init__(self):
        return

    line_template = '''package jp.co.happinet.commerce.app.api.dto.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.generated.jooq.product.enums.*;

import jp.co.happinet.commerce.fw.entity.util.DTO;

import java.util.Optional;


public interface LineDTO<LINE>
    extends DTO {{

    default int index() {{
        return this.lineNumberInt() - 1;
    }}

    int lineNumberInt();

    int quantityInt();

    @NotNull String productCode();

    @NotNull String productNameKana();

    @NotNull UnitCode unitCode();

    @NotNull Optional<String> remarksOpt();
}}


'''
    header_template = '''package jp.co.happinet.commerce.app.api.dto.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.generated.jooq.product_replacement_direction.enums.*;

import jp.co.happinet.commerce.app.domain.common.typed.code.SectionCode;
import jp.co.happinet.commerce.app.domain.common.typed.date.ReplacementDate;
import jp.co.happinet.commerce.fw.entity.util.DTO;

import java.util.List;
import java.util.Optional;


public interface HeaderDTO<HEADER extends HeaderDTO<HEADER, LINE>, LINE extends LineDTO<LINE>>
    extends DTO {{

    int MAX_LINE_COUNT = 98;

    @NotNull String warehouseCode();

    @NotNull SectionCode inventorySectionCode();

    @NotNull Optional<ReplacementDate> replacementDateOpt();

    @NotNull InputReplacementKind inputReplacementKind();

    // 【振替元】
    @NotNull List<LINE> fromLines();

    // 【振替先】
    @NotNull List<LINE> toLines();
}}

'''

    derived_line_template = '''package jp.co.happinet.commerce.app.api.dto.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.fw.entity.util.DTO;


public interface DerivedLine<LINE>
    extends DTO {{

    @NotNull LineDTO<?> beforeDerivedLine();

    @NotNull LINE beforeDerivedLine(@NotNull final LineDTO<?> beforeDerivedLine);
}}

'''

    derived_toLine_template = '''package jp.co.happinet.commerce.app.api.dto.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.domain.{domain_package}.ProductReplacementToAchievementLine;
import jp.co.happinet.commerce.fw.entity.util.DTO;


public interface DerivedToLine
    extends DTO, DerivedLine<DerivedToLine> {{

    static @NotNull DerivedToLine of(@NotNull final LineDTO<?> dto,
        @NotNull final ProductReplacementToAchievementLine line) {{

        return DTO.create(DerivedToLine.class)//
            .beforeDerivedLine(dto)//
            .productReplacementToAchievementLine(line);
    }}

    @NotNull DerivedToLine productReplacementToAchievementLine(@NotNull final ProductReplacementToAchievementLine line);

    @NotNull ProductReplacementToAchievementLine productReplacementToAchievementLine();
}}
    
'''

    derived_fromLine_template = '''package jp.co.happinet.commerce.app.api.dto.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.domain.{domain_package}.ProductReplacementFromAchievementLine;
import jp.co.happinet.commerce.fw.entity.util.DTO;


public interface DerivedFromLine
    extends DTO, DerivedLine<DerivedFromLine> {{

    static @NotNull DerivedFromLine of(@NotNull final LineDTO<?> dto,
        @NotNull final ProductReplacementFromAchievementLine line) {{

        return DTO.create(DerivedFromLine.class)//
            .beforeDerivedLine(dto)//
            .productReplacementFromAchievementLine(line);
    }}

    @NotNull DerivedFromLine productReplacementFromAchievementLine(
        @NotNull final ProductReplacementFromAchievementLine line);

    @NotNull ProductReplacementFromAchievementLine productReplacementFromAchievementLine();
}}

    
'''

    derived_header_template = '''package jp.co.happinet.commerce.app.api.dto.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.domain.{domain_package}.{class_name};
import jp.co.happinet.commerce.app.domain.{domain_package}.ProductReplacementFromAchievementHeader;
import jp.co.happinet.commerce.app.domain.{domain_package}.ProductReplacementToAchievementHeader;
import jp.co.happinet.commerce.fw.entity.util.DTO;

import java.util.List;

import static jp.co.happinet.commerce.fw.utils.MacroLike.*;


public interface DerivedHeader
    extends DTO {{

    static @NotNull DerivedHeader of(@NotNull final {class_name} productReplacementAchievement,
        @NotNull final HeaderDTO<?, ?> headerDTO) {{

        return DTO.create(DerivedHeader.class)//
            .beforeDerivedHeader(headerDTO)//
            .productReplacementAchievement(productReplacementAchievement)//
            .fromLines(list())//
            .toLines(list());
    }}

    @NotNull List<DerivedFromLine> fromLines();

    @NotNull List<DerivedToLine> toLines();

    @NotNull DerivedHeader fromLines(@NotNull List<DerivedFromLine> fromLines);

    @NotNull DerivedHeader toLines(@NotNull List<DerivedToLine> toLines);

    @NotNull HeaderDTO<?, ?> beforeDerivedHeader();

    @NotNull DerivedHeader beforeDerivedHeader(@NotNull final HeaderDTO<?, ?> beforeDerivedHeader);

    @NotNull {class_name} productReplacementAchievement();

    // TODO ProductReplacementFromAchievementHeaderを今回用のIFに置き換える
    default @NotNull ProductReplacementFromAchievementHeader fromHeader() {{
        return this.productReplacementAchievement().fromHeader();
    }}

    default @NotNull ProductReplacementToAchievementHeader toHeader() {{
        return this.productReplacementAchievement().toHeader();
    }}

    @NotNull DerivedHeader productReplacementAchievement(
        @NotNull final {class_name} productReplacementAchievement);

    default long fromTotalAmount() {{
        return sum(this.fromLines().stream()//
            .map(x -> x.productReplacementFromAchievementLine())//
            .mapToLong(x -> x.excludingTaxAmount()));
    }}

    default long toTotalAmount() {{
        return sum(this.toLines().stream()//
            .map(x -> x.productReplacementToAchievementLine())//
            .mapToLong(x -> x.excludingTaxAmount()));
    }}
}}

'''


