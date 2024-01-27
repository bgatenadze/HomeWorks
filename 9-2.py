# 2. დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sorted() ფუნქციის გამოყენებით (კლებადობით).

import random

# Generate a random list with 10 elements
random_list = [random.randint(1, 100) for _ in range(10)]

# Print the original list
print("Original List:", random_list)

# Sort the list in descending order
sorted_list = sorted(random_list, reverse=True)

# Print the sorted list
print("Sorted List (Descending):", sorted_list)
