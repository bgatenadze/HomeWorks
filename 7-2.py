# შექმენი ფუნქცია, რომელიც მიიღებს შეკვეთას, ანუ კერძის სახელს და 
# რაოდენობას და დაბეჭდავს მას, თუმცა რაოდენობას თუ არ მივუთითებთ,
# შეცდომას არ ამოაგდებს და 1_ად ჩათვლის.


def print_order():
    food_name = input("შეიყვანეთ კერძის სახელი: ")
    food_quantity_input = input("შეიყვანეთ კერძის რაოდენობა: ")
    
    food_quantity = int(food_quantity_input) if food_quantity_input else 1
    
    print(f"შეკვეთა: {food_quantity} {food_name}")


print_order()
