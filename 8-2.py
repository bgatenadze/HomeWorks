## 2. დაწერე პროგრამა ლამბდას გამოყენებით, რომელიც გადაცემული სიის სიგრძეს დააბრუნებს,
# მას შემდეგ რაც წაშლის სიიდან ყველა სახელს რომელიც პატარა სიმბოლოთი იწყება.
# (გამოიყენე .isupper() მეთოდი)

def count_capitalized_names(name_list):
    return len(list(filter(lambda name: name[0].isupper(), name_list)))

names = ["Georgia", "USA", "russia", "turkey"]

count_of_capitalized_names = count_capitalized_names(names)

print("სიის სიგრძეა:", count_of_capitalized_names)
