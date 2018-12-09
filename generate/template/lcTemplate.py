
class LCTemplate:

    def __init__(self):
        return

    method_template = '''/** {jp_name}  */
    @InputFixedLengthColumn(start = {str_position} , end = {end_position} )
    public String {method_name};

    '''
