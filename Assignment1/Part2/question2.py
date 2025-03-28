'''program that prompts user to enter two numbers and divde the first number by the second number and displays 2 decimal places'''
while True:
    try: 
        num = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        result = num / num2
        print(f'The result is {result:.2f}')
        break
    except ValueError:
        print('Invalid input. Please enter a valid number.')
    except ZeroDivisionError:
        print('Error: Division by zero is not allowed.')
    except Exception as e:
        print(f'An error occurred: {e}')

