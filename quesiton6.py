# program that prompts user for series of number but stores value which comes between 1 to 100 and display it

class Between:
    def __init__(self):
        self.main_list = []  

    def checked_list(self):
        for i in self.numbers_list:
            if 1 < i < 100:
                self.main_list.append(i)
        return self.main_list
    
    def getter(self):
        while True:
            try:
                self.numbers = input('Enter number seperated by space: ')
                self.numbers_list= list(map(int, self.numbers.split()))
                return
             
            except ValueError:
                print('Error! You can only enter number.')

            except Exception as e:
                print(f"Error! {e}")
    
    def ouput(self):
        print(f"List: {self.checked_list()}")
        
    def main(self):
        self.getter()
        self.ouput()

between = Between()
between.main()