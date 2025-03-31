# Program that prompts user to enter list of names, stores them in list and finds how many times letter a apperared in list

class Check_A:
    def __init__(self):
        # Initialize counter for letter 'a' occurrences
        self.count = 0

    def count_a(self):
        # Iterate through each name in the list
        for name in self.names_list:
            # Check each character in the name
            for char in name:
                # If character is 'a' (case insensitive), increment counter
                if char.lower() == "a":
                   self.count += 1

    def take_input(self):
        # Keep asking for input until valid names are provided
        while True: 
            try:
                # Get input from user and split into list of names
                self.names = input("Enter a names seprated by space: ")
                self.names_list = self.names.split()
                # Validate that all names contain only alphabetic characters
                if not all(name.isalpha() for name in self.names_list):
                    raise Exception ("Names can only contain alphabet.")
                return 
                
            except Exception as e:
                print(f"Error! {e}")
    
    def output(self):
        # Display the results with formatting
        print("\n_________________________________________________________________________________\n")
        print(f'List {self.names_list}')
        print(f'Times letter a apperared: {self.count}')
        print("_________________________________________________________________________________")
    
    def mainfunc(self):
        # Main execution flow: get input, count 'a's, and display results
        self.take_input()
        self.count_a()
        self.output()

# Create instance of Check_A class and run the program
check_a = Check_A()
check_a.mainfunc()

