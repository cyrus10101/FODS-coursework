# Class to manage temperature records for different days
class Temperature:
    def __init__(self):
        # Initialize an empty dictionary to store day-temperature pairs
        self.temp_dict = {}  
    
    def take_input(self):
        # Get day input from user, '0' to exit
        day = input("Enter day or(0 to exit): ")
        if day == '0':
            return None, None
        while True:
            try:
                # Get temperature value and convert to float
                temp_val = float(input("Enter temperature value: "))
                return day, temp_val  
                    
            except ValueError:
                # Handle case where temperature input is not a valid number
                print("Error! Temperature value must be a number.")
            
            except Exception as e:
                # Handle any other unexpected errors
                print(f"Error! {e}")

    def store_temp(self, day, temp_val):
        # Store temperature for a given day if it doesn't already exist
        if day not in self.temp_dict:  
            self.temp_dict[day] = temp_val
        else:
            print(f"Temperature for {day} already exists!")

    def display_output(self):
        # Display the dictionary of temperatures
        print(f"Dictionary of day respect to temperature: {self.temp_dict}")
        # Ask user if they want a formatted display
        option = input('Do you want to align day and temperature in more readable way(Y/N): ')
        if option.lower() == 'y':
            # Display temperatures in a formatted table-like structure
            print('\n-------------------------------------------------------------------')
            for i, j in self.temp_dict.items():
                print(f"{i}: {j}")
            print('-------------------------------------------------------------------')
        else:
            return 

    def mainfunc(self):
        # Main loop to continuously get temperature inputs until user exits
        while True:
            day, temp_val = self.take_input()
            if day == None:
                break
            self.store_temp(day, temp_val)     
        self.display_output()      

# Create instance of Temperature class and run the program
temperature = Temperature()
temperature.mainfunc()
