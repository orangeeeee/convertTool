class EndpointTemplate:

    def __init__(self):
        return

    clazz_template = '''package jp.co.happinet.commerce.app.endpoint.{package};

import org.jetbrains.annotations.NotNull;

import jp.co.happinet.commerce.app.api.business.{package}.{class_name}BusinessAPI;
import jp.co.happinet.commerce.app.api.query.product_replacement.{class_name}QueryAPI;
import jp.co.happinet.commerce.app.endpoint.ExecutionResult;
import jp.co.happinet.commerce.app.endpoint.dto.{class_name}ListCriteriaRequestDTO;
import jp.co.happinet.commerce.app.endpoint.dto.{class_name}ListDeleteRequestDTO;
import jp.co.happinet.commerce.app.endpoint.dto.{class_name}ListResponseDTO;
import jp.co.happinet.commerce.app.endpoint.dto.{class_name}RequestDTO;
import jp.co.happinet.commerce.app.endpoint.dto.{class_name}ResponseDTO;
import jp.co.happinet.commerce.fw.endpoint.Response;

import javax.annotation.Resource;
import javax.validation.Valid;

import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import static jp.co.happinet.commerce.app.endpoint.{package}.Abstract{class_name}Endpoint.*;


@Transactional
@RestController
@RequestMapping(PATH)
public class {class_name}Endpoint
    extends Abstract{class_name}Endpoint {{

    @Resource
    private {class_name}QueryAPI queryAPI;

    @Resource
    private {class_name}BusinessAPI businessAPI;

    @GetMapping
    public @NotNull Response<{class_name}ListResponseDTO> query(
        @NotNull final {class_name}ListCriteriaRequestDTO request) {{

        return Response.of({class_name}ListResponseDTO.of(this.queryAPI.findLimit(request), false));
    }}

    @PostMapping(value = "/header/@validate_derive")
    public @NotNull Response<{class_name}ResponseDTO> deriveHeader(
        @RequestBody @NotNull final {class_name}RequestDTO req) {{

        final var derived = this.businessAPI.deriveAndValidateHeader(req);

        return Response.of({class_name}ResponseDTO.ofDerivedHeader(req, derived));
    }}

    @PostMapping(value = "/@validate_derive")
    public @NotNull Response<{class_name}ResponseDTO> deriveAndValidateLine(
        @Valid @RequestBody @NotNull final {class_name}RequestDTO req) {{

        final var derived = this.businessAPI.deriveAndValidateLines(req);

        return Response.of({class_name}ResponseDTO.ofDerivedLine(req, derived));
    }}

    @PostMapping
    public @NotNull Response<ExecutionResult> register(
        @Valid @RequestBody @NotNull final {class_name}RequestDTO req) {{

        return Response.of(ExecutionResult.of(this.businessAPI.register(req)));
    }}

    @PutMapping("/@cancel")
    public @NotNull Response<ExecutionResult> cancel(
        @RequestBody @NotNull final {class_name}ListDeleteRequestDTO req) {{

        this.businessAPI.cancel(req.numbers());

        return Response.of(new ExecutionResult());
    }}

    @GetMapping(value = "/@no_validation/{{{class_name}Number}}")
    public @NotNull Response<{class_name}ResponseDTO> get(
        @NotNull @PathVariable("{class_name}Number")
        final String {class_name}Number) {{

        final var derived = this.businessAPI.get({class_name}Number);

        return Response.of({class_name}ResponseDTO.fromDB(derived));
    }}
}}



'''

    abstract_clazz_template = '''package jp.co.happinet.commerce.app.endpoint.{package};

import jp.co.happinet.commerce.app.api.query.product_replacement.{class_name}QueryAPI;

import javax.annotation.Resource;


public abstract class Abstract{class_name}Endpoint {{

    static final String PATH = "/product_replacement_work";

    @Resource
    {class_name}QueryAPI queryAPI;
}}

'''
