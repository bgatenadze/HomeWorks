#1. შექმენი ფუნქცია რომელიც მიიღებს სიას და დააბრუნებს ასევე სიას, თუმცა უნიკალური ელემენტებით
# (გამოიყენე set მონაცემთა ტიპი).

def unique_elements(input_list):
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list

original_list = [1, 2, 2, 3, 4, 4, 1, 7, 7, 5, 5]
result_list = unique_elements(original_list)
print(result_list)

