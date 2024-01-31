#1.	შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი პერიმეტრისა და ფართობის გამოსათვლელად.


import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def calculate_area(self):
        area = math.pi * (self.radius ** 2)
        return area

# Example usage:
radius_value = 5
my_circle = Circle(radius_value)

perimeter_result = my_circle.calculate_perimeter()
area_result = my_circle.calculate_area()

print(f"Circle with radius {radius_value}:")
print(f"Perimeter: {perimeter_result}")
print(f"Area: {area_result}")