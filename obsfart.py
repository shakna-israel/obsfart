#https://docs.python.org/2/reference/datamodel.html#emulating-numeric-types

# Rules:

# * a() (Operates as a + operator, and can take an unlimited number of inputs, in the form of a list.)
# * b() (Operates as a - operator, and can take an unlimited number of inputs, in the form of a list.)
# * c() (Operates as a * operator, and can take an unlimited number of inputs, in the form of a list.)
# * d() (Operates as a / operator, and can take an unlimited number of inputs, in the form of a list.)
# * e() (Takes a string value of more than two characters, or multiple strings (in the form of a list), and swaps every third character with the next.)
# * f() (Expects a,b,c,d or e, and can take an unlimited number of inputs, in the form of a list. Converts a() into b(), and c() into d(). Reverses the output of e().)
# * g() (Prints to stdout, in reverse order. Can take one input of int, string or list. In the case of a list input, each item is reversed, and the whole list is printed in reverse.)
# * h() (Prints to file, in reverse order. Can take two values (input, output) or a list, where the middle value, or in the case of an even list the first middle value represents the output file.)
# * i() (Reads in a data stream, either StreamIO or file object. Data stream is stored for evaluation - safety of which is left to the user. Takes one input, string or list of strings.)
# * j() (Evaluates a stored data stream, by splitting it into a,b,c,d,e,f,g,h,i,j and evaluating in order. Normal Python functions should be ignored, but j() isn't secure, and doesn't pretend to be.)
# * k() (Adds two or more strings together, after running them through e(). Takes two inputs, or a list.)
# * l() (Takes two strings or a list of strings. If given two strings, takes the first from the first. (e.g. string.replace("secondstring")). If given a list of strings, the middle value, or in the case of an even list, the first middle value is the substring to replace with.)

def a(x=None,y=None):
    """Takes two ints, or a list of ints"""
    if y:
        return x.__add__(y)
    else:
        result = 0
        for item in x:
            result = result.__add__(item)
        return result

print(a(6,4))
print(a([6,4]))
print(a(a(6,4),a([6,4])))
