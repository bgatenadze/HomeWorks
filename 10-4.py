#4.	დათვალე ძიების თითოეული მეთოდისთვის საჭირო დრო (დეკორატორის გამოყენებით) და დააკვირდი
# დროში სხვაობას მცირე, საშუალო და გრძელი სიის შემთხვევებში.


import random
import time

def generate_random_integers(n, start_range, end_range):
    random_integers = sorted([random.randint(start_range, end_range) for _ in range(n)])
    return random_integers

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} took {execution_time:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def linear_search(sorted_list, target):
    """
    Perform linear search to find the target element in a sorted list.
    """
    for i, num in enumerate(sorted_list):
        if num == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

@timing_decorator
def binary_search(sorted_list, target):
    """
    Perform binary search to find the target element in a sorted list.
    """
    low, high = 0, len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_element = sorted_list[mid]

        if mid_element == target:
            return mid  # Return the index if the target is found
        elif mid_element < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage:
random_list = generate_random_integers(1000, 1, 1000000)
target_element = random.choice(random_list)  # Choose a random element from the list

# Print the generated and sorted list
print("Generated and Sorted List:", random_list)

# Measure the time for linear search
linear_result = linear_search(random_list, target_element)
print(f"Linear Search Result: {linear_result}")

# Measure the time for binary search
binary_result = binary_search(random_list, target_element)
print(f"Binary Search Result: {binary_result}")


# მცირე სიის შემთხვევაში ძიების სისწრაფე მსგავსია.
# საშუალო და გრძელი სიის შემთხვევაში ბინარული სწრაფია.