Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
not True
False
not False
True
not 2>3
True
not 2<3
False
not 4=
SyntaxError: cannot assign to expression
not 4==3
True
x=10
y=20
if not y<x:
    print('IT worked')

    
IT worked


C=10
D=5
if C>10 and  D>1:
    print("It worked!")

    
if C>10 and  D>1:
    print("It worked!")

c=11
if C>10 and  D>1:
    print("It worked!")


    
if C>10 and  D>1:
    print("It worked!")

    

>>> if C>=10 and  D>1:
...     print("It worked!")
... 
...     
It worked!
>>> 
>>> 
>>> 
>>> if not(C>10 and  D>1):
...     print("It worked!")
... 
...     
It worked!
>>> 
>>> 
>>> 
>>> c=5
>>> d=-1
>>> if c>1 or d>1:
...     print("It worked")
... 
...     
It worked
>>> 
>>> 
>>> True or False
True
>>> 
>>> 
>>> 
>>> C=5
>>> D=2
>>> if (C>4 and D>4) or (C>1 and D>1):
...     print("IT worked")
... 
...     
IT worked
>>> if ((C>4 and D>4) or (C>1 and D>1)):
...     print("IT worked")
... 
...     
IT worked
>>> if not((C>4 and D>4) or (C>1 and D>1)):
...     print("IT worked")
... 
...     
