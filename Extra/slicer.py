Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
word="supercalifragilisticexpialidocious"
word[0]
's'
word
'supercalifragilisticexpialidocious'
word[2]
'p'
word[0:10:2]
'sprai'
word[5:9]
'cali'
word[5:]
'califragilisticexpialidocious'
word[5::]
'califragilisticexpialidocious'
word[5::2]
'clfaiitcxildcos'
word[:7]
'superca'
>>> word[::-1]
'suoicodilaipxecitsiligarfilacrepus'
>>> 
>>> 
>>> word[-2]
'u'
>>> word[-5]
'c'
>>> word[-1]
's'
>>> 
>>> 
>>> 
>>> word.index("cali")
5
>>> word.index("fragi")
9
>>> word[world.index("cali"):word.index("fragi")]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    word[world.index("cali"):word.index("fragi")]
NameError: name 'world' is not defined. Did you mean: 'word'?
>>> word[word.index("cali"):word.index("fragi")]
'cali'
>>> word[word.index("docious")]
'd'
>>> word[word.index("docious"):]
'docious'
>>> word[word.index("f"):word.index("e")]
''
>>> word.index("f")
9
>>> word[word.index("f"):word.index("exp")]
'fragilistic'
>>> 
>>> 
>>> 

... 
... 
>>> 
>>> 

... 
>>> 
