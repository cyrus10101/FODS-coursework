'''Program that prompts user to enter number and prints whether it is odd or even'''
# Boolean function to check where number is odd or even
def odd_or_even(para):
    if para % 2 == 0:
        return True
    else:
        return False
 # Loop that end when no exception are thrown
while True:
    try:
        num = int(input('Enter a number: '))
        if odd_or_even(num):
            print(f'{num} is an Even number.')
        else:
            print(f'{num} is an Odd numer.')
        break
    except ValueError: #Catches ValueError exception
        print('Error! You can only enter number.')

    except Exception as e: # Catches all exception other than ValueError and stores in object e
        print(f'Error: {e}')