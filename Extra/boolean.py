Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
B=True
c=False
D=true
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    D=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> D=True
>>> E="True"
>>> type(E)
<class 'str'>
>>> type(B)
<class 'bool'>
>>> 2>3
False
>>> 2<3
True
>>> type(2<3)
<class 'bool'>
>>> 2=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 2==3
False
>>> 3=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 3=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 3==3
True
>>> 
>>> 

... 
>>> 

>>> 

>>> 2!=3
True
>>> 4>=3
True
>>> 3>=3
True
>>> 2.=3
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> 2>=3
False
>>> 
>>> 
>>> 
>>> 
