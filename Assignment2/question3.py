# Program that checks whether number given number is armstrong or not using function
def convert(para):
    converted_value = 0
    length = len(str(para))

    while para != 0:
       reminder =  para % 10
       converted_value += reminder ** length # using ** instead of math to avoid getting float value and int conversion
       para //= 10 # using // to avoid getting float value
    return converted_value

def armstrong(para):
    return para == convert(para)

while True:
    try:
        number = int(input('Enter a number: '))

        if number < 0:
            raise Exception('Error! Negetive number cannot be entered.')
        
        if armstrong(number):
            print(f'{number} is an Armstrong number.')
        else:
            print(f'{number} is not an Armstrong number.')
        break

    except ValueError:
        print('Error! You can only enter number.')

    except Exception as e:
        print(f'Error! {e}')


