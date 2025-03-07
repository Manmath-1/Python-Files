Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
students={}
students={"Alice":25,"Bob":27,"Clarie":17,"Dan":21,"Emma":22}
error_students={Alice:25,Bob:27}
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    error_students={Alice:25,Bob:27}
NameError: name 'Alice' is not defined. Did you mean: 'slice'?
students
{'Alice': 25, 'Bob': 27, 'Clarie': 17, 'Dan': 21, 'Emma': 22}
students["Dan"]
21
students["Fred"]=25
students["Fred"]
25
students["Alice"]
25
students["Alice"]=26
students["Alice"]
26
delstudents['Fred']
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    delstudents['Fred']
NameError: name 'delstudents' is not defined. Did you mean: 'students'?
students
{'Alice': 26, 'Bob': 27, 'Clarie': 17, 'Dan': 21, 'Emma': 22, 'Fred': 25}
del students["Fred"]
students
{'Alice': 26, 'Bob': 27, 'Clarie': 17, 'Dan': 21, 'Emma': 22}
students.keys()
dict_keys(['Alice', 'Bob', 'Clarie', 'Dan', 'Emma'])
students.keys()[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    students.keys()[0]
TypeError: 'dict_keys' object is not subscriptable
a=list(students.keys())
a
['Alice', 'Bob', 'Clarie', 'Dan', 'Emma']
a[0]
'Alice'
>>> a[1]
'Bob'
>>> students.values()
dict_values([26, 27, 17, 21, 22])
>>> list(students.values())[2:]
[17, 21, 22]
>>> print(students)
{'Alice': 26, 'Bob': 27, 'Clarie': 17, 'Dan': 21, 'Emma': 22}
>>> students.items()
dict_items([('Alice', 26), ('Bob', 27), ('Clarie', 17), ('Dan', 21), ('Emma', 22)])
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
Traceback (most recent call last):
  File "C:/Users/omkar/Desktop/Python Bible/students.py", line 8, in <module>
    print(students["clarie"])
KeyError: 'clarie'
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
['ID003', 17, 'C']
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
ID003
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
ID003
[21, 'D']
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
Traceback (most recent call last):
  File "C:/Users/omkar/Desktop/Python Bible/students.py", line 2, in <module>
    'Alice':{"id":ID001,"age":26,"grade":"A"},
NameError: name 'ID001' is not defined
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
21
>>> 
=============== RESTART: C:/Users/omkar/Desktop/Python Bible/students.py ===============
21
ID005 E
