#3. დაწერე ფუნქცია, რომელიც გადაცემული სტრიქონისგან ლექსიკონს შექმნის და დააბრუნებს.
#ვთქვათ გადავეცით ფუნქციას სტრიქონი, უნდა დააბრუნოს სიმბოლოები key_ს ადგილას და 
# მათი რაოდენობა value_ს ადგილას.
#მაგალითად გადავეცით სტრიქონი : 'racoon'
#უნდა დააბრუნოს ლექსიკონი: {'r': 1, 'a': 1, ‘c': 1, 'o': 2, ‘n': 1}



def create_char_count_dict(input_string):
    char_count_dict = {}
    
    for char in input_string:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    
    return char_count_dict


user_input_str = input("Enter a string: ")
result_dict = create_char_count_dict(user_input_str)

print(f"String: '{user_input_str}'")
print("Character count dictionary:", result_dict)
