# კალკულატორი

def calculate_expression(input_data):
    # Check if there is an operator without spaces, e.g., 4*6
    for operator in ['+', '-', '*', '/', '^']:
        if operator in input_data:
            operator_index = input_data.find(operator)
            num1, num2 = input_data[:operator_index], input_data[operator_index + 1:]
            operation = operator
            break
    else:
        # If no operator found, assume there are spaces between num1, operation, and num2
        split_data = input_data.split()
        if len(split_data) != 3:
            return "Error: Invalid input format. Please enter an expression like '2 * 6' or '4*6'."

        num1, operation, num2 = split_data

    # Convert numbers to float
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Error: Please enter valid numbers."

    # Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operation == '^':
        result = num1 ** num2
    else:
        return f"Error: Invalid operation '{operation}'. Please use one of: +, -, *, /, ^."

    return result

# Example usage:
user_input = input("Enter an expression (e.g., 2 * 6 or 4*6): ")
result = calculate_expression(user_input)
print("Result:", result)
