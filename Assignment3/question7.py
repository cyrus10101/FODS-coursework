import csv
from tabulate import tabulate
class Employee:
    def ui(self):
        print("----------------------------------------\n")
        print("          press '1' to enter data       \n")
        print("          press '0' to See data         \n")
        print("          press other key to exit        ")
        print("\n----------------------------------------")

    def __init__(self):
        self.__employee_id = None
        self.__name = None
        self.__address = None
        self.__contact_number = None
        self.__number_of_child = None
        self.__salary = None
    
    def take_input(self):
        # Get employee information from user input
        self.__name = input("Enter employee name: ")
        self.__address = input("Enter employee address: ")
        self.__contact_number = input("Enter contact number: ")
        
        # Loop until user enter valid data
        while True:
            try:
                self.__employee_id = int(input("Enter employee ID: "))
                self.__number_of_child = int(input("Enter number of children: "))
                self.__salary = float(input("Enter salary: "))
                break
            except ValueError:
                print("Error! Please enter valid numbers.")
            except Exception as e:
                print(f"Error! {e}")
                
        # Write data to CSV file
        try:
            with open('employees.csv', 'a') as file:
                writer = csv.writer(file)
                writer.writerow([self.__employee_id, self.__name, self.__address, self.__contact_number,
                                self.__number_of_child, self.__salary])

        except Exception as e:
            print(f'Error! {e}.')

    def display_list(self):
        try:
            with open('employees.csv', 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                data_list = list(reader)
                data_list = list(filter(None, data_list))  # Only include rows that are not empty

                print(tabulate(data_list, headers=['ID', 'Name', 'Address', 'Contact Number', 'Number of child', 'Salary'], tablefmt='fancy_grid'))
        except FileNotFoundError: 
            print('Error! file not found so cannot read from file')
        except Exception as e:
            print(f'Error! {e}') 
    
    def mainfunc(self):
        self.ui()
        while True:
            choice = input('Your choice: ')
            if choice == '1':
                self.take_input()
            elif choice == '0':
                self.display_list()
            else:
                break
            print("----------------------------------------------------------------------------------------")

employee = Employee()
employee.mainfunc()