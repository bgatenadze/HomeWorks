consumer_info = []

for i in range(3):

    consumer = [] # დროებითი სია
    
    consumer.append(input("Enter Your Name: "))
    consumer.append(input("Enter Your Lastname: "))
    consumer.append(input("Enter Your Age: "))
    consumer_info.append(consumer)


consumer_index =  int(input("Enter Consumer Index from 0 to 2: "))

print(f"Name: {consumer_info[consumer_index][0]}")
print(f"Lastname: {consumer_info[consumer_index][1]}")
print(f"Age: {consumer_info[consumer_index][2]}")