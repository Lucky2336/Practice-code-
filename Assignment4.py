"""
Write a program that converts and prints user given measurement in inches into
1. foot(12 inches)
2. yard(36 inches)
3. centimetres(2.54 inches)
4. meter(39.37 inches)
"""

inches=float(input("Enter the measurement in inches: "))
foot=float(inches/12)
yard=float(inches/36)
cm=float(inches * 2.54)
meter=float(inches/39.37)

print(inches , "inches= " ,foot ," foot")
print(inches , "inches= " ,yard ," yards")
print(inches , "inches= " ,cm ," centimeters")
print(inches , "inches= " ,meter ," meters")

