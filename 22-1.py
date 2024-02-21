# კალკულატორი კლასებით და ფაილთან კავშირით

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x):
        self.result += x

    def subtract(self, x):
        self.result -= x

    def multiply(self, x):
        self.result *= x

    def divide(self, x):
        if x != 0:
            self.result /= x
        else:
            print("Error: Cannot divide by zero")

            # 1 ნაწილი

    def save_state(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self.result))
        print(f"Calculator state saved to {filename}")


            # 2 ნაწილი
            
    def load_state(self, filename):
        try:
            with open(filename, 'r') as file:
                self.result = float(file.read())
            print(f"Calculator state loaded from {filename}")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
        except ValueError:
            print(f"Error: Unable to parse data from file '{filename}'")

# Example usage:
calculator = Calculator()

calculator.add(5)
calculator.subtract(2)
calculator.multiply(3)
calculator.divide(2)

print("Current result:", calculator.result)

        # 1 ნაწილის ნაწილი
# Save state to a file
calculator.save_state('calculator_state.txt')

# Create a new calculator instance
new_calculator = Calculator()

        # 2 ნაწილის ნაწილი
    
# Load state from the file
new_calculator.load_state('calculator_state.txt')

# Check the result in the new calculator instance
print("Result after loading state:", new_calculator.result)
