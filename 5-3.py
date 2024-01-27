LA = ["Leila", "Abashidze", "1929 August 1"]
SCH = ["Sofiko", "Chiaureli", "1937 May 21"]
KK = ["Kakhi", "Kavsadze", "1935 June 5"]
VK = ["Vakhtang", "Kikabidze", "1938 July 19",]

database = [LA, SCH, KK, VK]

firstname_or_lastname = input("Enter First or Last Name (must start with capital letter): ")

for act in database:
    if firstname_or_lastname in act:
        print(f"Name: {act[0]}\nLastname: {act[1]}\n"
              f"Date of Birth: {act[2]}")
        break
else:
    print("No match found!")