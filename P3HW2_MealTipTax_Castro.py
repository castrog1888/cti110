# CTI-110 
# P3HW2 - MealTipTax 
# Gregory Castro 
# 6-20-2019
#
#This program will take your meal bill and calculate three different 
#tips:15%, 18% or 20%. If the anything other than 15%, 18% or 20%
#is inputed, then a Error will be issued. It will then calculate the 7%
#sales tax of the meal bill and then display the total bill. The values 
#will be displayed rounded 2 decimal places.
# Pseudocode
# 1.) Declare variables
#       meal_bill = 0.0 float
#       tip = 0.0 float
#       sales_tax = 0.07 float
#       
# 2.) Prompt the user for the meal bill and tip
# 3.) Calculate the tip based on user input of 15, 18, or 20. If any other
#       number, other than 15, 18, or 20, is inputed then a error will be
#       issued. Calculate the 7% sales tax of the meal bill. Calculate
#       the total bill.
# 4.) Display the tip, sales tax and the total bill.

#Title and information
print()
print("Meal, Tip and Tax Calculator:")
print('*This program will calculate your tip')
print(' (15%, 18% or 20%), Sales Tax, and Total Bill.')
print()

#Prompt the user for the meal bill and tip
print('Enter the meal cost:')
meal_cost = float(input("$ "))
print('Enter tip percentages as either 15, 18, or 20 ONLY.')
print('DO NOT enter the percentage symbol (%).')
tip = float(input('Tip:'))

#Calculations for sales tax and the total bill
sales_tax = 0.07 * meal_cost
total = meal_cost + sales_tax + (meal_cost * (tip/100))
print()

#Calculate the tip for 15%, 18% or 20%. Display error if not
#entered properly.
#Display the tip, sales tax and the total bill rounded two
#decimal places.

if tip == 15:
    print('15% Tip:$', round(meal_cost * (tip/100), 2))
    print('Sales Tax:$', round(sales_tax,2))
    print('Total Bill:$', round(total,2))
elif(tip == 18):
    print('18% Tip:$', round(meal_cost * (tip/100), 2))
    print('Sales Tax:$', round(sales_tax,2))
    print('Total Bill:$', round(total,2))
elif(tip == 20):
    print('20% Tip:$', round(meal_cost * (tip/100), 2))
    print('Sales Tax:$', round(sales_tax,2))
    print('Total Bill:$', round(total,2))
else:
    print('ERROR!!: You entered a invalid tip amount.')
    print('Enter ONLY 15, 18 or 20 for the tip.')
print()

#This code will hold the screen until any key is pressed
print("Press any key to close")
input()








