# calculator that takes two decimal number and does arthematic calculation using function and return calculated value.

# Creating a class named Calculator.
class Calculator:
    # Creating Function to do different calculation
    def add(self):
        return self.num1 + self.num2
    
    def sub(self):
        return self.num1 - self.num2
    
    def multi(self):
        return self.num1 * self.num2
    
    def divide(self):
        if self.num2 == 0:
            return " Error! second number cannot be zero."
        return self.num1 / self.num2
    
    def trancuted_division(self):
        if self.num2 == 0:
            return "Error! second number cannot be zero."
        return int(self.num1 /self.num2)
    
    def modulus_division(self):
        if self.num2 == 0:
            return "Error! second number cannot be zero."
        return self.num1 % self.num2
    
    def exponen(self):
        return self.num1 ** self.num2
    
    # Creating function that takes input
    def get_value(self):
        while True:
            try:
                self.num1 = float(input("Enter first number: "))
                self.num2 = float(input("Enter second number: "))

                # Using return instead of break because break is used in loop whereas we should use return in case of funciton
                return self.num1, self.num2

            except ValueError:
                print("Error! You can only enter number.")
            
            except Exception as e:
                print(f"Error! {e}")

    # Creating function to display calculated value
    def calculated_values(self):
        print(f"addition: {self.add()}")
        print(f"Subtraction: {self.sub()}")
        print(f"Multiplication: {self.multi()}")
        print(f"Divsion: {self.divide()}")
        print(f"Trancuted Division: {self.trancuted_division()}")
        print(f"Modulus Division: {self.modulus_division()}")
        print(f"Exponetiation: {self.exponen()}")

    # Main function to control flow of logic and function
    def main(self):
        self.get_value()
        self.calculated_values()


calculator = Calculator()
calculator.main()
