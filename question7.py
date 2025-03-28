# Program that prompts user to enter list of names, stores them in list and finds how many times letter a apperared in list

class Check_A:
    def __init__(self):
        self.count = 0

    def count_a(self):
        for name in self.names_list:
            for char in name:
                if char.lower() == "a":
                   self.count += 1

    def take_input(self):
        while True: 
            try:
                self.names = input("Enter a names seprated by space: ")
                self.names_list = self.names.split()
                if not all(name.isalpha() for name in self.names_list):
                    raise Exception ("Names can only contain alphabet.")
                return 
                
            except Exception as e:
                print(f"Error! {e}")
    
    def output(self):
        print("\n_________________________________________________________________________________\n")
        print(f'List {self.names_list}')
        print(f'Times letter a apperared: {self.count}')
        print("_________________________________________________________________________________")
    
    def mainfunc(self):
        self.take_input()
        self.count_a()
        self.output()

check_a = Check_A()
check_a.mainfunc()

