# რეკურსია

def welcome(n, counter=1):
    if counter > n:
        return
    
    print("Hello!")
    welcome(n, counter + 1)


n = int(input("შეიყვანეთ მისალმების რაოდენობა: "))

welcome(n)