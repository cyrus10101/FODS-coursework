'''Program that finds all the number between 1500 and 2000 (both included) that are divisible by 7 but not by 5 '''
def check(num):
    if num % 7 == 0 and num % 5 != 0:
        return True
    else:
        return False

for i in range(1500, 2001):
    if check(i):
        print(i)


