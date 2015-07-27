# ObsFart

ObsFart is an estoric functional programming system.

1. It's called ObsFart because its probably as code smelly as one of your worst farts. I'm not a mathematician, I shouldn't be writing something like this.
2. This is a spec that should be implementable in any functional programming language.

## Rules:

* All functions are strictly typed. If it expects an int, and you give a string, it'll simply raise an obtuse exception.
* The only exception produced by any of these functions should be an equivalent of *NotYetImplemented*
* a() (Operates as a + operator, and can take an unlimited number of inputs, in the form of a list.)
* b() (Operates as a - operator, and can take an unlimited number of inputs, in the form of a list.)
* c() (Operates as a * operator, and can take an unlimited number of inputs, in the form of a list.)
* d() (Operates as a / operator, and can take an unlimited number of inputs, in the form of a list.)
* e() (Takes a string value of more than two characters, or multiple strings (in the form of a list), and swaps every third character with the next.)
* f() (Expects a,b,c,d or e, and can take an unlimited number of inputs, in the form of a list. Converts a() into b(), and c() into d(). Reverses the output of e().)
* g() (Prints to stdout, in reverse order. Can take one input of int, string or list. In the case of a list input, each item is reversed, and the whole list is printed in reverse.)
* h() (Prints to file, in reverse order. Can take two values (input, output) or a list, where the middle value, or in the case of an even list the first middle value represents the output file.)
* i() (Reads in a data stream, either StreamIO or file object. Data stream is stored for evaluation - safety of which is left to the user. Takes one input, string or list of strings.)
* j() (Evaluates a stored data stream, by splitting it into a,b,c,d,e,f,g,h,i,j and evaluating in order. Normal Python functions should be ignored, but j() isn't secure, and doesn't pretend to be.)
* k() (Adds two or more strings together, after running them through e(). Takes two inputs, or a list.)
* l() (Takes two strings or a list of strings. If given two strings, takes the first from the first. (e.g. string.replace("secondstring")). If given a list of strings, the middle value, or in the case of an even list, the first middle value is the substring to replace with.)

## Python Implementation

The Python Implementation, ```obsfart.py```, if a work-in-progress to try and match the spec.

## Simple ObsFart Program

```obsfart
g(k("Herlo","Wolld"))
```

```
>> HelloWorld
```

*Note:* Obviously, ObsFart is far more about computation than string manipulation.
