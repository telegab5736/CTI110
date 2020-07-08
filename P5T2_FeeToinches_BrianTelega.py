#Feet to inches converter
#8JULY2020
#CTI-110 P5T2_FeetToInches 
#Brian Telega

#Constant
INCHES_PER_FOOT = 12

#Main function
#Get user input
def main():
    feet = int(input('Enter a number fo feet:'))
    print(feet, 'equals', feet_to_inches(feet), 'inches.')

#The feet_to_inches function converts feet to inches
def feet_to_inches(feet):
    return feet  * INCHES_PER_FOOT

#Call main function
main()



