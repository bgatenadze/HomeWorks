#1. დაწერე ფუნქცია რომელიც ლექსიკონიდან დუბლიკატებს ამოშლის და ყველა უნიკალური value_ს მქონე
# ლექსიკონს დააბრუნებს.


def remove_duplicates(dictionary):
    unique_values = set(dictionary.values())
    unique_dict = {key: value for key, value in dictionary.items() if list(dictionary.values()).count(value) == 1}
    return unique_dict


input_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 4}
result_dict = remove_duplicates(input_dict)

print("Original Dictionary:", input_dict)
print("Dictionary with Unique Values:", result_dict)
