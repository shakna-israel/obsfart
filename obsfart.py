from __future__ import division
import sys

class Obsfart(object):

    def __init__(self):
        sys.excepthook = self.exceptionHandler

    def exceptionHandler(self, exception_type, exception, traceback):
        debug = False
        if not debug:
            print("\n\nObsfart Error: NotYetImplemented")
            sys.exit(0)
        else:
            raise

    def a(self, x,y=None):
        """Takes two ints, or a list of ints"""
        x = int(x)
        y = int(y)
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
        if y:
            # Use a for loop to get the index of each character in both strings.
            # If the index number is a mod (%) of 3, then add it to a list. (One list for x, one for y.)
            # Rebuild strings from lists, and return both strings.
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
            raise NotImplementedError

fart = Obsfart()

print(fart.e(fart.e("Something","Cool")[0],fart.e("Something","Cool")[1]))

fart.a("string",1)
