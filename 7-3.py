## ფუნქცია, რომელიც იღებს მინიმუმ 3 რიცხვს და აბრუნებს და ბეჭდავს ნარმავლს.


def multiply_numbers():
    numbers = []

    # Ensure at least 3 numbers are entered
    while len(numbers) < 3:
        try:
            num = float(input("Enter a number: "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    result = 1
    for num in numbers:
        result *= num

    print(f"The multiplied result is: {result}")
    return result

# Function Call
multiply_numbers()
