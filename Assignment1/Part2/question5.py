'''program that finds simple interest when principal, rate and time are input by user'''

while True:
    try:
        principal = float(input('Enter the principal amount: '))
        rate = float(input('Enter the rate of interest: '))
        time = float(input('Enter the time period: '))
        simple_interest = (principal * rate * time) / 100
        print(f'The simple interest is {simple_interest}')
        break
    except ValueError:
        print('Invalid input. Please enter a valid number.')
    except Exception as e:
        print(f'An error occurred: {e}')