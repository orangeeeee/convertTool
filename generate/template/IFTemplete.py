class IFTemplate:

    def __init__(self):
        return

    interface_template = 'interface {clazzName} {{'

    method_template = '''/** {jp_name}  */
    @NotNull {type} {method_name}();
    
    @NotNull {clazzName} {method_name}(@NotNull final {type} {method_name});

    '''

    opt_method_template = '''/** {jp_name}  */
    @NotNull Optional<{type}> {method_name}Opt();

    @NotNull {clazzName} {method_name}Opt(@NotNull final {type} {method_name}Opt);

    '''
