# Function to collect daily temperatures for each day of the week
def get_daily_temp():
    # Initialize a dictionary with days of the week as keys and None as initial temperature values
    temp_dict = {
        'Sunday': None, 
        'Monday': None,
        'Tuesday': None,
        'Wednesday': None,
        'Thursday': None,
        'Friday': None,
        'Saturday': None
    }

    # Iterate through each day in the dictionary
    for i in temp_dict.keys():
       while True:
        try:
            # Get temperature input from user for each day
            # Convert input to float and store in dictionary
            temp = float(input(f'Enter temperature of {i}:'))
            temp_dict[i] = temp
            break
        except ValueError:
            # Handle case where user enters non-numeric input
            print("Error! Temperature value must be a number.")
        except Exception as e:
            # Handle any other unexpected errors
            print(f"Error! {e}")
    
    # Display the complete dictionary of temperatures
    print(f"\nDictionary of day respect to temperature: {temp_dict}")
    
    # Ask user if they want a more readable format
    option = input('Do you want to align day and temperature in more readable way(Y/N): ')
    
    # If user chooses 'Y', display temperatures in a formatted way
    if option.lower() == 'y':
        print('\n-------------------------------------------------------------------')
        for day, temp in temp_dict.items():
            print(f"{day}: {temp}")
        print('-------------------------------------------------------------------')
    
    return temp_dict

# Call the function to execute the program
get_daily_temp()