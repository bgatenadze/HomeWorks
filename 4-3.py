info1 = input("Enter info1: ")
info2 = input("Enter info2: ")
 
balanced = True
 
for symbol in info1:
    if symbol not in info2:
        balanced = False
 
for symbol in info2:
    if symbol not in info1:
        balanced = False
 
if balanced:
    print("Strings are balanced!")
else:
    print("Strings are not balanced!")