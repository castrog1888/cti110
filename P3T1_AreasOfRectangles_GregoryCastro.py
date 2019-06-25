# CTI-110 
# P3T1 - Areas Of Rectangles 
# Gregory Castro 
# 6-18-2019
#

#Pseudocode
# 1.)  Declare variables
#        length1 = 0.0 float
#        width1 = 0.0 float
#        area1 = 0.0 float
#        length2 = 0.0 float
#        width2 =  0.0 float 
#        area2 = 0.0 float
# 2.) Prompt user  to input length and width
#      values for rectangle 1 and 2.
# 3.) Calculate the area of rectangle 1 and 2.
#       area = lenght * width
#       rectangle1 will have the greater area, or
#       rectangle2 will have the greater area, or
#       both rectangles will have the same area.
# 4.) Determine which is the greater rectangle or if both are the same.
#       if area1 > area2
#                    Display "Rectangle 1 has the greatest area."
#       else if area2 > area1
#                    Display "Rectangle 2 has the greatest area."
#       else
#                    Display "Both rectangles have the same area."

#Title and information
print()
print('Areas of Rectangles:')
print('*This program will calculate the areas of 2 rectangles,')
print(' it will then determine and display the results.')
print()
#Declare variables
length1 = 0.0
width1 = 0.0
area1 = 0.0 
length2 = 0.0 
width2 =  0.0
area2 = 0.0 

#Prompt user for dimesions of rectangle 1 and 2
print('Rectangle 1:')
length1 = float(input('Enter the length: '))
width1 = float(input('Enter the width: '))
print('Rectangle 2:')
length2 = float(input('Enter the length: '))
width2 = float(input('Enter the width: '))
print()
#Calculate the areas of the rectangles
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area and then
#display the results
#1st method results
if area1 > area2:
     print('Rectangle 1 has the greater area.')
elif area2 > area1:
     print('Rectangle 2 has the greater area.')
else:
     print('Both have the same area.')
#or
#2nd method results
##if area1 > area2:
##     print('Rectangle 1 has the greater area.')
##else:
##     if area2 > area1:
##          print('Rectangle 2 has the greater area.')
##     else:
##          print('Both have the same area.')
print('The area of rectangle 1 is:', round(area1,2))
print('The area of rectangle 2 is:', round(area2,2))
print()

#This code will hold the screen until any key is pressed
print("Press any key to close...")
input()







