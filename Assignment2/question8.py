# Class to compare two lists and perform various operations on them
class Two_List:
    def __init__(self):
        # Initialize an empty list to store common numbers between the two lists
        self.__same_num = []
    
    # Method to check and compare the lengths of both lists
    def chk_length(self):
        length1 = len(self.__lst1)
        length2 = len(self.__lst2)
        if length1 == length2:
            return f"Length of List are same: {length1}."
        else:
            return f"Length of two list are not same.\nLength of List1: {length1}\nLength of List2: {length2}"
        
    # Method to check and compare the sum of elements in both lists
    def chk_sum(self):
        lst1_sum = sum(self.__lst1)
        lst2_sum = sum(self.__lst2)
        if lst1_sum == lst2_sum:
            return f"sum of both number is same: {lst1_sum}"
        else:
            return f"sum of both list are different\nlist 1: {lst1_sum}\nList 2: {lst2_sum}"
        
    # Method to find common values between the two lists
    def chk_value(self):
        same_value = False
        # Nested loops to compare each element of first list with second list
        for number in self.__lst1:
            for number2 in self.__lst2:
                if number == number2:
                    self.__same_num.append(number)
                    same_value = True

        if same_value:
            return f"Values that are in both list they are: {self.__same_num}"
        else:
            return "There are not any same value in Lists."
        
    # Method to take user input for both lists
    def take_input(self):
        while True:
            try: 
                # Get input from user and convert space-separated numbers into lists
                lst1 = input("Enter numnbers in List 1: ")
                lst2 = input("Enter numbers for List 2: ")
                self.__lst1 = list(map(int, lst1.split()))
                self.__lst2 = list(map(int, lst2.split()))
                return 
            
            except ValueError: 
                print('Error! only number are allowded to enter.')
            
            except Exception as e:
                print(f"Error! {e}")
    
    # Method to display all comparison results
    def output(self):
        print()
        print("----------------------------------------------------------------------------------------")
        print(f"{self.chk_length()}\n")
        print(f"{self.chk_sum()}\n")
        print(f"{self.chk_value()}\n")
        print("----------------------------------------------------------------------------------------")
        
    # Main method to control flow of methods or logic
    def main_func(self):
        self.take_input()
        self.output()

# Create an instance of Two_List and run the program
two_list = Two_List()
two_list.main_func()