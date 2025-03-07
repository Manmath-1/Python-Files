Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def about(name, age, likes):
...     sentence="Meet They are {} years old and they like{}".format(name, age, likes)
...     return sentence
... 
>>> about("jack",23,""python)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> about("jack",23,"python")
'Meet They are jack years old and they like23'
>>> def about(name, age, likes):
...     sentence="Meet {}! They are {} years old and they like {}".format(name, age, likes)
...     return sentence
... 
>>> about("jack",23,"python")
'Meet jack! They are 23 years old and they like python'
>>> 
>>> 
>>> def about(name, age, likes="python"):
...     sentence="Meet {}! They are {} years old and they like {}".format(name, age, likes)
...     return sentence
... 
>>> about("jack",23,)
'Meet jack! They are 23 years old and they like python'
>>> about("jack",23,"Football")
'Meet jack! They are 23 years old and they like Football'
