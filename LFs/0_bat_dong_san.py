from __init__ import *


@labeling_function()
def key_word_0(x):
    '''
    LFs Bất động sản
    '''
    if x['check_btype'] == 'Bất động sản':
        keyword = ['tiền thuế', 'phí']
        keyword.extend(convert(keyword))
        for i in keyword:
            if i in x['name_cleaned']: 
                return 0
    elif x['check_btype'] != 'Bất động sản':
        pass
    return -1
    
