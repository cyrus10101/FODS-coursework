# Program that takes string input and finds total number of uppercase and lowercase letter using function

def find_upper(para):
    lower = sum(i.isupper() for i in para)
    return lower

def find_lower(para):
    upper = sum(i.islower() for i in para)
    return upper

string = input('Enter a number: ')
print(f'Total Uppercase letter: {find_upper(string)}')
print(f'Total Lowercase letter: {find_lower(string)}')
