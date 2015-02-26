

def flatten_list(a, result=None):
    if result is None:
        result = []
    for x in a:
        if isinstance(x, list):   
        else:
            result.append(x)
    return result



