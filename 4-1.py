info = input("Enter info: ")
 
al = 0
dig = 0
other = 0
 
for symbol in info:
    if symbol.isdigit():
        dig += 1
    elif symbol.isalpha():
        al += 1
    else:
        other += 1
 
print(f"""
Alphabetic Symbols: {al}
Digits: {dig}
Other: {other}
""")