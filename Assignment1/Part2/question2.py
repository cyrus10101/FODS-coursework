'''
Program that prompts user for two numbers and divides frst
number by second, with exactly two decimal value displayed
'''
# Function to divide two number
def divide(para1, para2):
    return para1 /  para2

# Loop that only breaks if no exception are thrown
while True:
    try: 
        num1 = float(input('Enter your first number: '))
        num2 = float(input('Enter your second number: '))
        print(f'{num1} Divide by {num2} is {divide(num1, num2):.2f}')# :.2f -> this prints 2 decimal value
        break
    except ValueError:# Catches ValueError error
        print('Error! You can only enter number.')
    except ZeroDivisionError: # Catches ZeroDivisionError error
        print('Error! second number cannot be zero.')
    except Exception as e:# Catches other exception 
        print(f'Error! {e}')
    