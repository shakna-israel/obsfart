def a(x=None,y=None):
    """Takes two ints, or a list of ints"""
    if y:
        return x.__add__(y)
    else:
        result = 0
        for item in x:
            result = result.__add__(item)
        return result
