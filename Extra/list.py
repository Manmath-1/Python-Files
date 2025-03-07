Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
our_list=[27,46,-5,17,99]
print(our_list)
[27, 46, -5, 17, 99]
type(our_list)
<class 'list'>
jackson=['A','B','C',1,2,3,"do",True,False]
jaclson[2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    jaclson[2]
NameError: name 'jaclson' is not defined. Did you mean: 'jackson'?
jackson[4]
2
jackson[6]
'do'
>>> jackson[-2]
True
>>> x=jackson[6]
>>> x
'do'
>>> jackson[0:3]
['A', 'B', 'C']
>>> jackson
['A', 'B', 'C', 1, 2, 3, 'do', True, False]
>>> our_list=[1,2,[3,4,5],6,7,8]
>>> our_list[2]
[3, 4, 5]
>>> our_list[2[0]]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    our_list[2[0]]
TypeError: 'int' object is not subscriptable
>>> our_list[2][0]
3
>>> our_list[2][1]
4
>>> our_list[2][1:]
[4, 5]
>>> our_list[][1:]
SyntaxError: invalid syntax
>>> our_list[2][0::2]
[3, 5]
>>> 
>>> 
>>> 
>>> 
>>> our_table=[[1,2,3],[4,5,6],[7,8,9]]
>>> our_table[0]
[1, 2, 3]
>>> our_table[1]
[4, 5, 6]
>>> our_table[2]
[7, 8, 9]
>>> our_table[0][1]
2
>>> our_table[1][2]
6
>>> our_table[2][1]
8
>>> our_table[1][1:]
[5, 6]
