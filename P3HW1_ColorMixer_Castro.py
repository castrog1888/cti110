# CTI-110 
# P3HW1 - Color Mixer 
# Gregory Castro 
# 6-18-2019
#
#This program will mix the inputed primary colors:
#"red", "blue" or "yellow" and then tell you the
#secondary color it reates.
#Pseudocode
# 1.) Declare variables
#      primary color = red, blue and yellow
#      secondary color = purple, orange and green
#      purple = red and blue 
#      orange = red and yellow
#      green = blue and yellow
#      anything else = error
# 2.) Prompt user for primary colors (red, blue or yellow)
# 3.) Determine the secondary color or display error
#      primary color and/or primary color = secondary color
#      any other colors = error
# 4.) Display the secondary color

#Title and information
print('Color Mixer:')
print('*This program will mix the Primary Colors: "red", "blue"')
print(' or "yellow" and tell you the Secondary Color it creates.')
print()

#Declare variables
##primary color = red, blue and yellow
##secondary color = purple, orange and green
##purple = red and blue 
##orange = red and yellow
##green = blue and yellow
##anything else = error

#Prompt the user to enter 2 primary colors
print('Please ONLY enter one of the following Primary Colors:')
print('"red", "blue", or "yellow"')
primary_color_one = input("Enter the 1st Primary Color: ")
primary_color_two = input("Enter the 2nd Primary Color: ")
print()

#Calculations:
#secondary colors will be displayed based upon
#inputs from primary colors. Error will also display
#if anything other than red, blue or yellow is inputed.
if(primary_color_one == "red" and primary_color_two == "blue") or \
  (primary_color_one == "blue" and primary_color_two == "red"):
    print('When you mix the primary colors red and blue,')
    print('it makes the secondary color purple.')
elif(primary_color_one == "red" and primary_color_two == "yellow") or \
     (primary_color_one == "yellow" and primary_color_two == "red"):
       print('When you mix the primary colors red and yellow,')
       print('it makes the secondary color orange.')
elif(primary_color_one == "blue" and primary_color_two == "yellow") or \
     (primary_color_one == "yellow" and primary_color_two == "blue"):
       print('When you mix the primary colors blue and yellow,')
       print('it makes the secondary color green.')
else:
       print('Error: One of the colors you entered is not a primary color.')
       print('Please ONLY enter red, blue, or yellow.')
print()

#This code will hold the screen until any key is pressed
print("Press any key to close")
input()

##if(primary_color_one == "red" and primary_color_two == "blue") or \
##  (primary_color_one == "blue" and primary_color_two == "red"):
##    print(primary_color_one + " mixed with " + primary_color_two + " is purple.")
##elif(primary_color_one == "red" and primary_color_two == "yellow") or \
##     (primary_color_one == "yellow" and primary_color_two == "red"):
##       print(primary_color_one + " mixed with " + primary_color_two + " is orange.")
##elif(primary_color_one == "blue" and primary_color_two == "yellow") or \
##     (primary_color_one == "yellow" and primary_color_two == "blue"):
##       print(primary_color_one + " mixed with " + primary_color_two + " is green.")
##else:
##       print("Error: One of the colors you entered is not a primary color. " + \
##                "Please enter red, blue, or yellow.")
       

