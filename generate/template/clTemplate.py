
class CLTemplate:

    def __init__(self):
        return

    method_template = '''/** {jp_name}  */
    @OutputFixedColumn(byteSize = {byteSize}, mode = Mode.{attr_mode})
    public String {method_name};

    '''
