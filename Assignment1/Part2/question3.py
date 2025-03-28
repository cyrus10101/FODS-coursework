'''program that converts celsius value to fahrenheit'''

while True:
    try:
        celsius = float(input('Enter the temperature in Celsius: '))
        fahrenheit = (celsius * 9/5) + 32
        print(f'The temperature in Fahrenheit is {fahrenheit}')
        break
    except ValueError:
        print('Invalid input. Please enter a valid number.')
    except Exception as e:
        print(f'An error occurred: {e}')

