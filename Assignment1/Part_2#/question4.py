'''
program that finds euclidean distance between two
coordinates and coorindates are input by user
'''
# Importing math to use math.sqrt()
import math

# Function to calculate distance
def distance(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Loop that breaks if no exception are raise or thrown
while True:
    try:
        print('X coordinate:')
        x1 = float(input('Enter x1: '))
        x2 = float(input('Enter x2: '))
        print('Y Coordinate:')
        y1 = float(input('Enter y1: '))
        y2 = float(input('Enter y2: '))

        # checking none any variable are negetive if found raising exeption
        if x1 < 0 or x2 < 0 or y1 < 0 and y2 < 0:
            raise Exception('You cannot enter negetive value')
        print(f'Distance between X and Y coordinate is{distance(x1, x2, y1, y2)}')
        break
    except ValueError:# Cathes ValueError Exception and handles in this block
        print('Error! You can only enter number.')
    except Exception as e:# Cathes if any other unexcepted Exception are thrown and handles
        print(f'Error! {e}')