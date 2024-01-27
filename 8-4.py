##4 დაწერე ბანკის ექაუნთის შექმნის, ანგარიშზე თანხის განთავსების
# და შემდგომ ექაუნთში შესვლის პროგრამა, არასწორი ინფორმაციის შეყვანა
# მომხმარებლისგან დააზღვიე try და except ბლოკის მეშვეობით


def get_valid_input(prompt, validation_function):
    while True:
        try:
            user_input = input(prompt)
            if validation_function(user_input):
                return user_input
            raise ValueError("Invalid input.")
        except ValueError as e:
            print(e)

user_dict = {}

try:
    user_dict["Username"] = get_valid_input("Enter username: ", lambda u: u.isalnum())
    user_dict["Password"] = get_valid_input("Enter password: ", lambda p: p.isalnum())
    user_dict["acc_balance"] = get_valid_input("Enter deposit amount: ", lambda d: float(d) >= 0)
    print("Account created successfully!")
except KeyboardInterrupt:
    print("\nProcess interrupted.")
    exit()

counter = 0

while counter < 3:
    try:
        username, password = input("Enter username: "), input("Enter password: ")
        if user_dict["Username"] == username and user_dict["Password"] == password:
            print("Logged in!\nAccount balance:", user_dict["acc_balance"], "GEL")
            break
        counter += 1
    except KeyboardInterrupt:
        print("\nProcess interrupted.")
        exit()

else:
    print("Wrong credentials 3 times.\nAccount blocked!\nContact customer service!")
