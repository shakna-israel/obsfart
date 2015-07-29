# ObsFart

ObsFart is an estoric functional programming library.

1. It's called ObsFart because its probably as code smelly as one of your worst farts. I'm not a mathematician, I shouldn't be writing something like this.
2. This is a spec that should be implementable in any functional programming language.
3. I wrote it because I could. As for should... See 1.

## Rules:

* All functions are strictly typed. If it expects an int, and you give a string, it'll simply raise an obtuse exception.
* The only exception produced by any of these functions should be an equivalent of *NotYetImplemented*.

### Functions Available:

* a() (Operates as a + operator, and can take an unlimited number of inputs, in the form of a list.)

e.g.
```
>> a(1,1)
   2
>> a([1,1,1,1,1,1,1])
   7
```
* b() (Operates as a - operator, and can take an unlimited number of inputs, in the form of a list.)

e.g.
```
>> b(1-1)
   0
>> b([100,1,1,1,1])
   96
```

* c() (Operates as a * operator, and can take an unlimited number of inputs, in the form of a list.)

e.g.
```
>> c(2,1)
   2
>> c([2,2,2])
   8
```

* d() (Operates as a / operator, and can take an unlimited number of inputs, in the form of a list.)

e.g.
```
>> d(20,10)
   2
>> d([200,1,1])
   0.005
```

* e() (Takes either two string values of more than two characters, or multiple strings (in the form of a list), and swaps every third character with the next.)

e.g.
```
>> e("Herlo","Wolld")
   Hello World
>> e(["Hello","World","String","Values"])
   (Hello, World, Stginr, Vaeusl)
```

* f() (Expects a,b,c,d,e,g or h, and can take an unlimited number of inputs, in the form of a list. Converts a() into b(), and c() into d(). Reverses the output 
of e(). Swaps h() and g().)

* g() (Prints to stdout, in reverse order. Can take one input of int, string or list. In the case of a list input, each item is reversed, and the whole list is printed in reverse.)

e.g.
```
>> g(1024)
   4201
>> g("String")
   gnirtS
>> g([1024,"String"])
   ["gnirtS",4201]
```

* h() (Prints to file, in reverse order. Can take two values (input, output) or a list, where the middle value, or in the case of an even list the first middle value represents the output file.)

e.g.
```
>> h("This belongs in a file", outFile")
   cat outFile
       This belongs in a file
>> h(["This belongs in a file", outFile, "This also belongs in a file."])
   cat outFile
       This belongs in a file
       This also belongs in a file.
>> h(["This belongs in a file", outFile, "This also belongs in a file.", "As does this."])
   cat outFile
       This belongs in a file
       This also belongs in a file.
       As does this.
```

* i() (Reads in a data stream, either a stream or file object. Data stream is stored for evaluation - safety of which is left to the user. Takes one input, string or list of strings.)

e.g.
```
>> stream = "g(2014)"
>> i(stream)
   "g(2014)"
>> stream = ["g(2014)","g(1024)"]
>> i(stream)
   "g(2014)",g"1024")
```

*Note*: In some languages, i() will be useless. In others, it will be useless without j(). In all languages, it is ***unsafe*** to use directly on user input.

* j() (Evaluates a stored data stream, by splitting it into a,b,c,d,e,f,g,h,i,j,k,l,m and evaluating in order. Normal functions should be ignored, but j() isn't secure, and doesn't pretend to be.)

e.g.
```
>> stream = i("g(1024)")
>> j(stream)
   4201
```

*Note*: In some languages, j() will be useless. In all languages, it is ***unsafe*** to use directly on user input.

* k() (Adds two or more strings together, after running them through e(). Takes two inputs, or a list.)

e.g.
```
>> k("String","Nostring")
   StsiniNortrgng
>> k(["String","Nostring","Others"])
   StginrNoitrsngOtserh
```

* l() (Takes two strings or a list of strings. If given two strings, takes the first from the first. If given a list of strings, the middle value, or in the case of an even list, the first middle value is the substring to replace with.)

e.g.
```
>> l("String","Str")
   ing
>> l(["String","Str","Substring"])
   ["ing", "Subing"]
>> l(["String","Str","Substring","Stroop"])
   ["ing","Subing","oop"]
```

## Python Implementation

The Python Implementation, ```obsfart.py```, found in the [python](python) folder, is a work-in-progress to try and match the spec.

## Simple ObsFart Program

```python
g(k("Herlo","Wolld"))
```

```
>> HelloWorld
```

*Note:* Obviously, ObsFart is far more about computation than string manipulation.

## License

Both the spec and the Python Implementation are in the Public Domain, and can be used for any purpose without restriction.

See the [LICENSE](LICENSE)
