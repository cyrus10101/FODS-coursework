Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = input('Enter your name: ')
Enter your name: cyrus
>>> uni_name = name.encode("utf-16")
>>> print(uni_name)
b'\xff\xfec\x00y\x00r\x00u\x00s\x00'
