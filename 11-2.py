#2. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე set ტიპის მონაცემს უნიკალური ელემენტებით,
# რომლის შეცვლაც შეუძლებელი იქნება (გამოიყენე frozenset).


def immutable_set(input_list):
    unique_set = set(input_list)
    unique_frozenset = frozenset(unique_set)
    return unique_frozenset


original_list = [1, 1, 2, 2, 3, 2, 5, 4, 4, 5]
result_frozenset = immutable_set(original_list)

print("Unique Frozenset:", result_frozenset)
