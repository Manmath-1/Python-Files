Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A="part one"
>>> B="part two"
>>> A+B
'part onepart two'
>>> A+ B
'part onepart two'
>>> A*3
'part onepart onepart one'
>>> "="*20
'===================='
>>> print("TITLE")
TITLE
>>> A="part"
>>> B=1
>>> A+B
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    A+B
TypeError: can only concatenate str (not "int") to str
>>> A+str(B)
'part1'
>>> "{}-{}".format(A.B)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    "{}-{}".format(A.B)
AttributeError: 'str' object has no attribute 'B'
>>> "{}-{}".format(A,B)
'part-1'
>>> "{}-{}".format(B,A)
'1-part'
>>> "{1}-{0}".format(A,B)
'1-part'
