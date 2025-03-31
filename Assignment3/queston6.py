# Student class to manage student information and display student details.
class Student:
    def __init__(self):
        # Initialize private instance variables with None values.
        self.__id = None
        self.__name = None
        self.__address = None
        self.__admission_year = None
        self.__level = None
        self.__section = None
        # Initialize dictionary to store student data.
        self.__data_dict = dict(id = None, Name = None, Address = None, Admission_year = None, Level = None, Section = None)
    
    def take_input(self):
        # Get student information from user input.
        self.__name = input(f'Enter student name: ')
        self.__address = input(f'Enter student Address: ')
        self.__section = input(f'Enter student Section: ')
        # Loop until valid integer inputs are received.
        while True:
            try: 
                # Get integer for id, admission year, and level.
                self.__id = int(input(f'Enter student Id: '))
                self.__admission_year = int(input(f'Enter student Admission year: '))
                self.__level = int(input(f'Enter student Level: '))
                break

            except ValueError: 
                print(f'Error! You can only enter integer number.')

            except Exception as e: 
                print(f'Error! {e}')

    def store_data(self):
        # Store all student information in the data dictionary.
        self.__data_dict = {
            "id": self.__id,
            "Name": self.__name,
            "Address": self.__address,
            "Admission_year": self.__admission_year,
            "Level": self.__level,
            "Section": self.__section
        }

    def display_output(self):
        # Display student information in a formatted way.
        print('\n_____________________________________________________________________________________________________________\n')
        print('Student Details.')
        for i, j in self.__data_dict.items():
            print(f"{i}: {j}")
        print('_____________________________________________________________________________________________________________')            
    
    def mainfunc(self):
        # Main function to control flow of logic.
        self.take_input()
        self.store_data()
        self.display_output()

# Create a Student instance and execute the main function.
student = Student()
student.mainfunc()
