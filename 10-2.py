# 2.	დაასორტირე შექმნილი სია რომელიმე ოპტიმალური მეთოდით. 

import random

def generate_random_integers(n, start_range, end_range):
    random_integers = [random.randint(start_range, end_range) for _ in range(n)]
    return random_integers

random_list = generate_random_integers(10, 1, 1000)

# Sort the list in ascending order
sorted_random_list = sorted(random_list)

print("Original List:", random_list)
print("Sorted List:", sorted_random_list)
