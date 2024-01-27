
ask_category = input("""აირჩიეთ თქვენთვის სასურველი პროდუქტი:
    1. ლეპტოპები
    2. პერსონალური კომპიუტერები
    3. მობილურები
""")

offer_product = ()

if ask_category == "1" or ask_category == "2" or ask_category == "3":
    ask_budget = int(input("შეიყვანეთ თქვენი მაქსიმალური ბიუჯეტის ოდენობა"))

# ამ ნაწილის ↓ ოპტიმიზაცია როგორ შეიძლება??

    if ask_category == "1" and ask_budget >=5000:
        offer_product = "Apple Premium Class - 7000 Lari"
    elif ask_category == "1" and ask_budget >= 2000:
        offer_product = "HP Model - 2500 Lari"
    elif ask_category == "1" and ask_budget >=700:
        offer_product = "Asus Model Economy - 800 Lari"

    elif ask_category == "2" and ask_budget >=4000:
        offer_product = "APPLE Desktop - 5500 Lari"
    elif ask_category == "2" and ask_budget >= 1800:
        offer_product = "PC SAMSUNG - 2300 Lari"
    elif ask_category == "2" and ask_budget >=600:
        offer_product = "PC ASUS - 1400 Lari"
    
    elif ask_category == "3" and ask_budget >=3000:
        offer_product = "IPHONE - 8000 Lari"
    elif ask_category == "3" and ask_budget >= 1500:
        offer_product = "Samsung Galaxy - 2100 Lari"
    elif ask_category == "3" and ask_budget >=300:
        offer_product = "Nokia - 250 Lari"
    else:
        offer_product = ("ამ თანხაში არ გაგვაჩნია შემოთავაზება")
else:
    offer_product = ("აირჩიეთ მოცემული კატეგორიებიდან ერთ-ერთი")

print (offer_product)