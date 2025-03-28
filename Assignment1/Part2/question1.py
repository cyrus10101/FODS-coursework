'''A program that continuously prompts the user for a number and determines if it's even or odd.
The program will keep asking until a valid integer is provided or the user chooses to exit.
To exit, the user can enter 'q' or 'quit'.
'''

def is_even_or_odd(num: int) -> str:
    """Determine if a number is even or odd and return a descriptive message."""
    return f"{num} is an {'even' if num % 2 == 0 else 'odd'} number."

def main():
    print("Welcome to the Even/Odd Number Checker!")
    print("Enter 'q' or 'quit' to exit the program.")
    
    while True:
        try:
            user_input = input("\nEnter a number: ").strip().lower()
            
            # Check for exit command
            if user_input in ['q', 'quit']:
                print("Thank you for using the program. Goodbye!")
                break
                
            # Convert input to integer
            num = int(user_input)
            
            # Print result
            print(is_even_or_odd(num))
            break  # Break the loop only if no exception is thrown
            
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'q' to quit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

