Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def fact(para):
...     factorial = 1
...     for i in range(1, para+1):
...         factorial *= i
...     return factorial
... 
>>> difference = fact(7) - fact(5)
>>> print(f'7 factorial minus 5 factorial is {difference}')
7 factorial minus 5 factorial is 4920
>>> 
