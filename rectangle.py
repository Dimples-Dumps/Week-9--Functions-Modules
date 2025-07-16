#Rectangle Area

import calculator

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectanglr: "))

area = calculator.area(length, width)
parimeter = calculator.parimeter(length, width)

print(f"The area of the rectangle is: {area}")
print(f"The parimeter of the rectangle is: {parimeter}")