from __future__ import division
import sys

class Obsfart(object):

    def __init__(self):
        sys.excepthook = self.exceptionHandler

    def exceptionHandler(self, exception_type, exception, traceback):
        debug = True
        if not debug:
            print("\n\nError: NotYetImplemented")
            sys.exit(0)
        else:
            raise

    def a(self, x,y=None):
        """Takes two ints, or a list of ints"""
        if y:
            x = int(x)
            y = int(y)
        else:
            x = list(x)
        if y:
            return x.__add__(y)
        else:
            result = 0
            for item in x:
                result = result.__add__(item)
            return result

    def b(self, x,y=None):
        """Takes two ints, or a list of ints"""
        if y:
            return x.__sub__(y)
        else:
            result = 0
            for item in x:
                result = result.__sub__(item)
            return result

    def c(self, x,y=None):
        """Takes two ints, or a list of ints"""
        if y:
            return x.__mul__(y)
        else:
            result = 1
            for item in x:
                result = result.__mul__(item)
            return result

    def d(self, x,y=None):
        """Takes two ints, or a list of ints"""
        if y:
            return x.__truediv__(y)
        else:
            result = 1
            for item in x:
                result = result.__truediv__(item)
            return result

    def e(self, x, y=None):
        """Takes two strings, or a list of strings"""
        if y:
            x = list(x)
            x2 = list(x)
            y = list(y)
            x_index = []
            x_iter = 0
            for i in x:
                x_iter = x_iter + 1
                x_index.append(x_iter)
            y_index = []
            y_iter = 0
            for i in y:
                y_iter = y_iter + 1
                y_index.append(y_iter)
            for item in x_index:
                if not item % 3:
                    try:
                        replace_with = y[item -1]
                    except IndexError:
                        replace_with = x[item -1]
                    x2[item -1] = replace_with
            for item in y_index:
                if not item % 3:
                    try:
                        replace_with = x[item -1]
                    except IndexError:
                        replace_with = y[item -1]
                    y[item -1] = replace_with
            x = "".join(x2)
            y = "".join(y)
            return (x, y)
        else:
            for item in x:
                orig = list(item)
                copy = list(item)
                index = []
                iter = 0
                return_list = []
                for i in orig:
                    iter = iter + 1
                    index.append(iter)
                for item in index:
                    if not item % 3:
                        try:
                            to_replace
                        except UnboundLocalError:
                            to_replace = None
                        if to_replace:
                            copy[item -1] = to_replace
                            to_replace = False
                        else:
                            to_replace = orig[item -1]
                return_list.append("".join(copy))
            return return_list

    def f():
        raise NotImplementedError

    def g():
        raise NotImplementedError

    def h():
        raise NotImplementedError

    def i():
        raise NotImplementedError

    def j():
        raise NotImplementedError

    def k():
        raise NotImplementedError

    def l():
        raise NotImplementedError
