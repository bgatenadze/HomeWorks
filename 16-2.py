#2.	შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების მეთოდებით.

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Cannot divide by zero")
        return num1 / num2

# Example usage:
calculator = Calculator()

# Addition
result_add = calculator.add(5, 3)
print(f"Addition: {result_add}")

# Subtraction
result_subtract = calculator.subtract(10, 4)
print(f"Subtraction: {result_subtract}")

# Multiplication
result_multiply = calculator.multiply(6, 7)
print(f"Multiplication: {result_multiply}")

# Division
result_divide = calculator.divide(15, 3)
print(f"Division: {result_divide}")
