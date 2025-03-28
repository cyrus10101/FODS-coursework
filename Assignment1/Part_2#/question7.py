# program that accepts string from users and calculates total digits and letters

string = input('Enter your string: ')

digits = sum(i.isdigit() for i in string)
letters = sum(i.isalpha() for i in string)

print(f'Total digit is {digits}')
print(f'Total letters is {letters}')
