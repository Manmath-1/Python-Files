Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(1,2,3,4,5)
1 2 3 4 5
>>> numbers=[1,2,3,4,5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> print(*numbers)
1 2 3 4 5
>>> print("abc")
abc
>>> print(*"abc")
a b c
>>> print("a","b","c")
a b c
>>> def add(x,y):
...     return x+y
... 
>>> def add(numbers):
...     total=0
...     for number in numbers:
...         total=total+number
...     return (total)
... 
>>> add(1,2,3,4,5,6,7,8,9)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    add(1,2,3,4,5,6,7,8,9)
TypeError: add() takes 1 positional argument but 9 were given
>>> def add(*numbers):
...     total=0
...     for number in numbers:
...         total=total+number
...     return (total)
... 
>>> add(1,2,3,4,5,6,7,8,9)
45
>>> 
>>> 
>>> 
>>> 
>>> def foo(**kwargs):
...     for key,value in kwargs.items():
...         print("{}:{}".format(key,value))
... 
...         
>>> foo(huda="female",ziyad="male")
huda:female
ziyad:male
