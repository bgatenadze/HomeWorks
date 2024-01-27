#საბანკო ანგარიში

bank_acc = 3000

while True:
    expense = int(input("What is your expanses?: "))
    if expense == 0 or bank_acc == 0:
        print(f"Your balance is {bank_acc}")
        break
        
    if expense > bank_acc:
        print("not enough money")
        continue
    else:
        bank_acc -= expense