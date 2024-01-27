# დაწერე პროგრამა, რომელიც დააჯამებს სიაში არსებულ დადებით და
# უარყოფით რიცხვებს ცალ-ცალკე. გამოიყენე ლამბდა ფუნქცია და filter.


def sum_of_positive_and_negative(numbers):
    sum_of_positives = sum(filter(lambda n: n > 0, numbers))
    sum_of_negatives = sum(filter(lambda n: n < 0, numbers))
    return sum_of_positives, sum_of_negatives

numbers = [10, -7, 17, -23]

positive_sum, negative_sum = sum_of_positive_and_negative(numbers)

print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)
