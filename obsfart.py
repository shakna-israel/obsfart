from __future__ import division

def a(x,y=None):
    """Takes two ints, or a list of ints"""
    if y:
        return x.__add__(y)
    else:
        result = 0
        for item in x:
            result = result.__add__(item)
        return result

def b(x,y=None):
    """Takes two ints, or a list of ints"""
    if y:
        return x.__sub__(y)
    else:
        result = 0
        for item in x:
            result = result.__sub__(item)
        return result

def c(x,y=None):
    """Takes two ints, or a list of ints"""
    if y:
        return x.__mul__(y)
    else:
        result = 1
        for item in x:
            result = result.__mul__(item)
        return result

def d(x,y=None):
    """Takes two ints, or a list of ints"""
    if y:
        return x.__floordiv__(y)
    else:
        result = 1
        for item in x:
            result = result.__truediv__(item)
        return result
