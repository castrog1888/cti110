# CTI-110 
# P3LAB - Debugging 
# Gregory Castro 
# 6-21-2019
#
#This program takes a numerical grade and outputs a letter grade.
#The system uses 10-point grading scale

##def score():

print('Numerical to Letter Grade:')
print()

#Declare variables
A_score = 90
B_score = 80
C_score = 70
D_score = 60 

#Prompt the user to input the numerical score
score = int(input('Enter your numberical score: '))

if score >= A_score:
    print('Your grade is: A')
else:
    if score >= B_score:
        print('Your grade is: B')
    else:
        if score >= C_score:
            print('Your grade is: C')
        else:
            if score >= D_score:
                print('Your grade is: D')
            else:
                print('Your grade is: F')

### program start
##score()

#This code will hold the screen until any key is pressed
print("Press any key to close...")
input()


