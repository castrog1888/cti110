# This program will calculate 23% profit of total sales
# 6-13-2019
# CTI-110 P2T1 - Sales Prediction
# Gregory Castro
#

#Get the projected total sales.
total_sales = float(input('Enter the total sales: '))

#Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

#Display the profit
print('The profit is $', format(profit, ',.2f'))
