# This program will convert pounds to kilograms
# 6-13-2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Gregory Castro
#

#This program will convert pounds to kilograms
#by taking the inputed amount of pounds and
#multiplying by 0.45359.

#Title display
print("Pounds (lbs) to Kilogram (kg) Converter:")

#Enter the amount of pounds to convert
lbs = float(input("Enter pounds (lbs): "))

#Calculate the kilograms conversion
kg = lbs / 2.2046

#Display the convertered kilograms (kg:_____)
print('Converted to kilograms (kg):', kg)

#This code will hold the screen until any key is pressed
print("Press any key to continue...")
input()
