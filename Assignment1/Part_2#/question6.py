'''Program that finds all the number between 1500 and 2000
 (both included) that are divisible by 7 and multiple by 5 
'''

# Function to check whether number is divisible by 7 and multiple of 5 or not.
def check(para):
    if para % 7 == 0 and para % 5 == 0:
        return True
    else:
        return False
    
# loop to print number in range between 1500 to 2001 if condition is met.
for i in range(1500, 2001):
    if check(i):
        print(i) 