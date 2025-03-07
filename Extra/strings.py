Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x="happy birthday"
x.capitalize()
'Happy birthday'
x
'happy birthday'








x
'happy birthday'
>>> x.title()
'Happy Birthday'
>>> x=x.title()
>>> x
'Happy Birthday'
>>> x.islower()
False
>>> x.isupper()
False
>>> x.istitle()
True
>>> x.isalpha()
False
>>> "abcd".isalpha()
True
>>> x.isdigit()
False
>>> "123".isdigit()
True
>>> y="happybirthday123"
>>> y.isalnum()
True
>>> 
>>> Y="happybirthday!123"
>>> y.isalnum()
True
>>> y
'happybirthday123'
>>> Y.isalnum()
False
>>> x.upper
<built-in method upper of str object at 0x000001DBE4F877B0>
>>> x,upper()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x,upper()
NameError: name 'upper' is not defined. Did you mean: 'super'?
>>> x.upper()
'HAPPY BIRTHDAY'
>>> x.lower()
'happy birthday'
>>> x=x.lower()
>>> x
'happy birthday'
>>> y.count("p")
2
