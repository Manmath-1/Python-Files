Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
our_tuple=1,2,3,"A","B","C"
type(our_tuple)
<class 'tuple'>
our_tuple=(1,2,3,"A","B","C")
type(our_tuple)
<class 'tuple'>
our_tuple[0:3]
(1, 2, 3)
our_list=[1,2,3,4,5,6,7]
>>> our_list[2]=100
>>> our_list
[1, 2, 100, 4, 5, 6, 7]
>>> our_tuple[2]=100
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    our_tuple[2]=100
TypeError: 'tuple' object does not support item assignment
>>> "12
SyntaxError: unterminated string literal (detected at line 1)
>>> s="1234567"
>>> s[2]="a"
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s[2]="a"
TypeError: 'str' object does not support item assignment
>>> A=[1,2,3]
>>> tuple(A)
(1, 2, 3)
>>> A
[1, 2, 3]
>>> A=tuple(A)
>>> A
(1, 2, 3)
>>> (A,B,C)=1,2,3
>>> A
1
>>> B
2
>>> C
3
>>> D,E,F=[1,2,3]
>>> D
1
>>> E
2
>>> F
3
>>> G,H,I="789"
>>> 
>>> H
'8'
>>> I
'9'
>>> G
'7'
