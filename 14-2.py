import csv

with open('names.csv', 'r', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('names.txt', 'w') as txt_file:
        for row in csv_reader:
            txt_file.write(','.join(row) + '\n')

print("ინფორმაცია გადმოკოპირებულია.")