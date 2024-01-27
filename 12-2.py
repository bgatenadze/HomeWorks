#2.დაწერე ფუნქცია რომელიც შეამოწმებს გადაცემული ლექსიკონი ცარიელია თუ არა და დააბრუნებს შესაბამის პასუხს.


def is_dict_empty(input_dict):
    return not bool(input_dict)

empty_dict = {}
non_empty_dict = {'a': 1, 'b': 2}

print("Is the dictionary empty?", is_dict_empty(empty_dict))
print("Is the dictionary empty?", is_dict_empty(non_empty_dict))
