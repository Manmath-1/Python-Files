Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
A=[5,12,54,84,2,44]
A=A+1
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    A=A+1
TypeError: can only concatenate list (not "int") to list
A=A+[1]
A
[5, 12, 54, 84, 2, 44, 1]
A=A+"BCD"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    A=A+"BCD"
TypeError: can only concatenate list (not "str") to list
A=A+["BCD"]
A
[5, 12, 54, 84, 2, 44, 1, 'BCD']
A=A+list("BCD")
A
[5, 12, 54, 84, 2, 44, 1, 'BCD', 'B', 'C', 'D']
A=A+(123)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    A=A+(123)
TypeError: can only concatenate list (not "int") to list
A=A+(1,2,3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    A=A+(1,2,3)
TypeError: can only concatenate list (not "tuple") to list
>>> A=A+[1,2,3]
>>> A
[5, 12, 54, 84, 2, 44, 1, 'BCD', 'B', 'C', 'D', 1, 2, 3]
>>> A=A+list(str(123))
>>> A
[5, 12, 54, 84, 2, 44, 1, 'BCD', 'B', 'C', 'D', 1, 2, 3, '1', '2', '3']
>>> A=[5,12,54,84,2,44]
>>> A
[5, 12, 54, 84, 2, 44]
>>> A=A+[5,6,7,8]
>>> A
[5, 12, 54, 84, 2, 44, 5, 6, 7, 8]
>>> A=A+[[5,6,7,8]]
>>> A
[5, 12, 54, 84, 2, 44, 5, 6, 7, 8, [5, 6, 7, 8]]
>>> A[-1]
[5, 6, 7, 8]
>>> A.append([7,8])
>>> A
[5, 12, 54, 84, 2, 44, 5, 6, 7, 8, [5, 6, 7, 8], [7, 8]]
>>> A=[5,12,54,84,2,44]A
SyntaxError: invalid syntax
>>> A=[5,12,54,84,2,44]
>>> A
[5, 12, 54, 84, 2, 44]
>>> A=A.append(10)
>>> A
>>> type(A)
<class 'NoneType'>
>>> A=[5,12,54,84,2,44]
>>> A
[5, 12, 54, 84, 2, 44]
>>> A.insert(2,100)
>>> A
[5, 12, 100, 54, 84, 2, 44]
>>> A.insert(2,[10,11,12])
>>> A
[5, 12, [10, 11, 12], 100, 54, 84, 2, 44]
>>> A.remove(12)
>>> A
[5, [10, 11, 12], 100, 54, 84, 2, 44]
>>> A=A.remove(5)
>>> A
>>> type(A)
<class 'NoneType'>
