#3. შექმენი ფუნქცია რომელიც მიიღებს ორ set ტიპის მონაცემს, გააერთიანებს მათ, შემდეგ კი გადააქცევს 
# tuple ტიპის მონაცემად და დააბრუნებს შედეგს.


def set_to_tuple(set1, set2):
    combined_set = set1.union(set2)
    result_tuple = tuple(combined_set)
    return result_tuple

set1 = {1, 2, 2, 3}
set2 = {3, 4, 5, 5, 5}
result = set_to_tuple(set1, set2)

print("Combined Tuple:", result)
