print("To register on the platform set username and password.\n"
      "Username must be non-empty and password must be of at least 8 charachters.\n"
      "If you no longer want to register enter \"exit\" for username or password "
      "and platform will shut down.")

while True:
    
    username = input("Enter Your Username (must be non-empty): ")

    if username == "exit":
        exit()

    password = input("Enter Your Password (must be at least 8 chars): ")

    if password == "exit":
        exit()

    if len(username) > 0 and len(password) >= 8:

        database = [username, password]
        print("Registration completed successfully!")
        break    

# პლატფორმაზე შესვლა

number_of_log_attempts = 3
i = 0

while i < number_of_log_attempts:
    
    username_log = input("Enter Your Username: ")
    password_log = input("Enter Your Password: ")

    i += 1
    
    if username_log == database[0] and password_log == database[1]:
    
        print("You are logged in!")
        break
    
    else:
    
        print(f"Username or Password is wrong. Try again (attempts left: {number_of_log_attempts - i}): ")

else: 

    print(f"Your have attempted to login {number_of_log_attempts} times. Try again later!")