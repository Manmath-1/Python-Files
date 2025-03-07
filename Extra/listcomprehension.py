Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> even_numbers=[x for x in range(1,51)if x%2==0]
>>> print(even_numbers)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> odd_numbers=[x for x in range(1,51)if x%2!=0]
>>> print(odd_numbers)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
>>> words=["the","quick","brown","fox","jumps","over","the","lazy","dog"]
>>> answer
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    answer
NameError: name 'answer' is not defined
>>> answer=[[w.upper(),w.lower(),len(w)]for w in words]
>>> print(answer)
[['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]
>>>  [[w.upper(),w.lower(),len(w)]for w in words]
...  
SyntaxError: unexpected indent
>>> [[w.upper(),w.lower(),len(w)]for w in words]
[['THE', 'the', 3], ['QUICK', 'quick', 5], ['BROWN', 'brown', 5], ['FOX', 'fox', 3], ['JUMPS', 'jumps', 5], ['OVER', 'over', 4], ['THE', 'the', 3], ['LAZY', 'lazy', 4], ['DOG', 'dog', 3]]
