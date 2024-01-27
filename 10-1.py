#1.	დაწერე ფუნქცია რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას. 

import random

def generate_random_integers(n, start_range, end_range):
    
    random_integers = [random.randint(start_range, end_range) for _ in range(n)]
    return random_integers

random_list = generate_random_integers(10, 1, 1000)
print(random_list)

