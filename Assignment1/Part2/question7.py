'''program that accepts string from users and calculates total digits and letters'''

while True:
    try:
        string = input('Enter a string: ')
        # Get all digits and letters
        all_digits = ''.join(c for c in string if c.isdigit())
        all_letters = ''.join(c for c in string if c.isalpha())
        # Count digits and letters
        digits = sum(c.isdigit() for c in string)
        letters = sum(c.isalpha() for c in string)
        print(f'Total digits: {digits}')
        print(f'Total letters: {letters}')
        print(f'Digits found: {all_digits if all_digits else "None"}')
        print(f'Letters found: {all_letters if all_letters else "None"}')
        break
    except Exception as e:
        print(f'An error occurred: {e}')


