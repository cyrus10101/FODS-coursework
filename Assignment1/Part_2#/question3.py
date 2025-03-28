'''
Program that converts Celsius to fahrenheit
'''
# Function that converts celsius to fahrenheit
def celsius_to_fahrenheit(para):
    return (para * 9/5) + 32

# Loop that end if no exception are thrown
while True:
    try:
        celsius = float(input('Enter Celsuis: '))
        print(f'Fahrenheit: {celsius_to_fahrenheit(celsius)}')
        break
    except ValueError:# Catches ValueError and handles in this block
        print('Error! You can only enter number.')
    except Exception as e: # Catches Error it there are any other exception and handles in this block
        print(f'Error! {e}')
    