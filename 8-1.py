
### chatgpt-ს მიჩვევა ცოდნია ...

# დაწერე პროგრამა, რომელიც გადაამრავლებს სიის ყველა წევრს კონკრეტულ რიცხვზე ლამბდას გამოყენებით.

def multiply_by_number(numbers, n=1):
    numbers_by_n = list(map(lambda m: m*n, numbers))
    return numbers_by_n

numbers = [3, 7, 11] #სია

result = multiply_by_number(numbers, n=3) #ვამრავლებთ 3-ზე

print("Original List:", numbers, "\nFinal List:", result)