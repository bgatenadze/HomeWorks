#დაწერე კომენტარად შუალედური პროექტის აღწერა და ატვირთე პროექტის საწყისი კოდი.

# შუალედურის პროექტს ვაკეთებ კალკულატორს, რომელსაც ექნება ყველა სტანდარტული ფუნქცია, მათ შორის
# ხარისხში აყვანა და ფესვის ამოღება.

# ნიკა, ეს პროექტი საკმარისი იქნება შუალედური გამოცდისთვის???


import math

def calculator(num1, num2, operation):
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Cannot divide by zero"
    elif operation == 'power':
        result = num1 ** num2
    elif operation == 'sqrt':
        if num1 >= 0:
            result = math.sqrt(num1)
        else:
            return "Error: Cannot calculate square root of a negative number"
    elif operation == 'root':
        if num1 >= 0 and num2 != 0:
            result = num1 ** (1 / num2)
        else:
            return "Error: Cannot calculate root for negative number or root with exponent 0"
    else:
        return "Error: Invalid operation"

    return result

# Example usage:
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide, power, sqrt, root): ")

result = calculator(num1, num2, operation)
print(f"Result: {result}")
