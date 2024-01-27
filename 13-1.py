#1.	დაწერე ფუნქცია რომელიც მომხმარებელს ჩააწერინებს ტექსტურ ფაილში ინფორმაციას Input ფუნქციის დახმარებით,
# მანამ სანამ მომხმარებელი არ შეიყვანს სიტყვას _ “enough”.

def func1():

    with open("new_file.txt", 'w') as file:
        while True:
            data = input("შეიყვანეთ ინფორმაცია (დასასრულებლად შეიყვანეთ 'enough'): ")

            if data.lower() == 'enough':
                break

            file.write(f"{data}\n")
    return

func1()
