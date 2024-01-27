#2.	დაწერე ფუნქცია რომელიც input ფუნქციის დახმარებით მომხმარებლისგან მიიღებს საქაღალდის ლოკაციას და
# შესაქმნელი ფაილის სახელს, შემდეგ მიღებულ ლოკაციაზე შექმნის შესაბამის ფაილს და ამოპრინტავს საქაღალდეში
# არსებულ ყველა ფაილის სიას.

import os

def func2():
    folder_location = input("შეიყვანეთ საქაღალდის მისამართი: ")
    file_name = input("შეიყვანეთ შესაქმნელი ფაილის სახელი: ")

    file_url = folder_location + '/' + file_name

    with open(file_url, 'x') as file:
        print(f"ფაილი '{file_name}' შექმნილია")

        files_in_folder = os.listdir(folder_location)
        print(f"\nსაქაღალდეში არსებული ფაილების სიაა: {files_in_folder}")
    return

func2()
