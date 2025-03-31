# Program to store numbers between 1-100 from user input

class Between:
    def __init__(self):
        self.main_list = []  # Store filtered numbers

    def checked_list(self):
        # Store numbers between 1-100
        for i in self.numbers_list:
            if 1 < i < 100:
                self.main_list.append(i)
        return self.main_list
    
    def getter(self):
        # Get and validate user input
        while True:
            try:
                self.numbers = input('Enter number seperated by space: ')
                self.numbers_list = list(map(int, self.numbers.split()))
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

# Run program
between = Between()
between.main()