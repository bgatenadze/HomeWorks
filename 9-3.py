##3.	დაწერე პროგრამა რომელიც შეადგენს შემთხვევით მთელ რიცხვთა სიას და შექმნილი სიის სორტირება
# სცადე ორი განსხვავებული მეთოდით (მაგ. Bubble და Selection). დათვალე თითოეული მეთოდისთვის
# სორტირებისთვის საჭირო დრო და დააკვირდი რომელი უფრო ეფექტურია მცირე(1000 ელემენტი),
# საშუალო(2000 ელემენტი) და გრძელი(3000 ელემენტი) სიის შემთხვევებში.

import random
import time

def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

def main():
    sizes = [1000, 2000, 3000]

    for size in sizes:
        random_list = generate_random_list(size)
        
        # Bubble Sort
        bubble_time = measure_time(bubble_sort, random_list.copy())
        print(f"Bubble Sort time for {size} items: {bubble_time:.6f} seconds")

        # Selection Sort
        selection_time = measure_time(selection_sort, random_list.copy())
        print(f"Selection Sort time for {size} items: {selection_time:.6f} seconds")

        print("------------")

if __name__ == "__main__":
    main()


## სამივე შემთხვევაში უფრო ეფექტურია Selection Sort მეთოდი