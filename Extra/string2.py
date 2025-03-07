Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x="happybirthday"
>>> x.index("birthday")
5
>>> x.find("birthday")
5
>>> x.find("birthday")
5
>>> X.find("Birthday")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X.find("Birthday")
NameError: name 'X' is not defined. Did you mean: 'x'?
>>> x.find("Birthday")
-1
>>> Y="00000happybirthday00000"
>>> y.strip("0")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    y.strip("0")
NameError: name 'y' is not defined. Did you mean: 'Y'?
>>> Y.strip('0')
'happybirthday'
>>> Y.lstrip("0")
'happybirthday00000'
>>> Y.rstrip("0")
'00000happybirthday'
>>> Y
'00000happybirthday00000'
>>> name=input("What is your name?")
What is your name?
>>> name=input("What is your name?:")
What is your name?:Zee 
>>> print(name)
Zee 
>>> len(name)
4
>>> name=input("What is your name?:").strip()
What is your name?:Zee    
>>> print(name)
Zee
>>> len.(name)
SyntaxError: invalid syntax
>>> len(name)
3
