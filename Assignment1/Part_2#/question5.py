'''program that finds simple interest when principal, rate and time are input by user'''

# Function that calculates simple interest
def simple_intrest(principle, rate, time):
    return (principle * rate * time) / 100
# Loop that breaks if no exception are thrown
while True:
    try:
        principle = int(input('Enter principle: '))
        rate = int(input('Enter rate: '))
        time = int(input('Enter time: '))
        print(f'Simple intrest: {simple_intrest(principle, rate, time)}')
        break
    except ValueError:# Handles ValueError in this block
        print('Error! You can only enter number.')
    except Exception as e:# Handles exception which is not handled by ValueError
        print(f'Error! {e}')
