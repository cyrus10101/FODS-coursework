import math
def check_prime(para):
    if para <= 1:
        return False
    for i in range(2, int(math.sqrt(para)) + 1):
        if para % i == 0:
            return False
    return True

while True:
    try:
        num = int(input('Enter a number: '))
        if check_prime(num):
            print(f'{num} is a prime number.')
        else:
            print(f'{num} is not a prime number')
        break

    except ValueError:
        print('Error! You can only enter number.')

    except Exception as e:
        print(f'Error! {e}')

