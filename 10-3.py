#3.	დასორტირებულ სიაში ელემენტის მოსაძებნად გამოიყენე ხაზობრივი და ბინარული ძიება. 

import random

def generate_random_integers(n, start_range, end_range):
    random_integers = sorted([random.randint(start_range, end_range) for _ in range(n)])
    return random_integers

def linear_search(sorted_list, target):
    """
    Perform linear search to find the target element in a sorted list.
    """
    for i, num in enumerate(sorted_list):
        if num == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

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
random_list = generate_random_integers(10, 1, 1000)
target_element = random.choice(random_list)  # Choose a random element from the list

# Print the generated and sorted list
print("Generated and Sorted List:", random_list)

# Linear search
linear_result = linear_search(random_list, target_element)
print(f"Linear Search Result: {linear_result}")

# Binary search
binary_result = binary_search(random_list, target_element)
print(f"Binary Search Result: {binary_result}")
