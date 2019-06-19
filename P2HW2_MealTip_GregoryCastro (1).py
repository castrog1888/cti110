# This program will calculate the tips for meals
# Date
# CTI-110 P2HW2 - Meal Tip Calculator
# Gregory Castro
#

#This program will calculate the tip amounts of the meal total
#for 3 different percentages (15%, 18% and 20%). It will also
#give the meal bill total for all 3 tip percentages. The values will
#be displayed rounded 2 decimal places.

#Title display
print("Meal Tip Calculator:")
print()

#Enter the meal bill total
meal_total = float(input("Enter the Meal Bill total: $ "))

#Calculate tip of the meal bill
fifeteen_percent_tip = meal_total * .15
eighteen_percent_tip = meal_total * .18
twenty_percent_tip = meal_total * .2

#Display the tip of the meal bill, rounded 2 decimal places
print('15% Tip:$', round(fifeteen_percent_tip,2))
print('18% Tip:$', round(eighteen_percent_tip,2))
print('20% Tip:$', round(twenty_percent_tip,2))

#Add the meal bill plus the tip
fifteen_percent_total = meal_total + fifeteen_percent_tip
eighteen_percent_total = meal_total + eighteen_percent_tip
twenty_percent_total = meal_total + twenty_percent_tip

#Display the total of the meal bill plus the tip, rounded 2 decimal places
print('Meal Bill + 15% Tip Total:$', round(fifteen_percent_total,2))
print('Meal Bill + 18% Tip Total:$', round(eighteen_percent_total,2))
print('Meal Bill + 20% Tip Total:$', round(twenty_percent_total,2))

#or
##print('Meal Bill + 15% Tip Total:$', format(fifteen_percent_total,'.2f'))
##print('Meal Bill + 18% Tip Total:$', format(eighteen_percent_total,'.2f'))
##print('Meal Bill + 20% Tip Total:$', format(twenty_percent_total,'.2f'))







