#Program provinding the comparison of two rectangles area's
#18June2020
#CTI-110 P3T1-Area of a Rectangle
#Brian Telega

#Get the dimensions of R1.
length1 = int(input('Enter the length of rectangle 1:'))
width1 = int(input('Enter the width of rectangle 1:'))

#Get the dimensions of R2
length2 = int(input('Enter the length of rectangle 2:'))
width2 = int(input('Enter the width of rectangle 2:'))

#Calculate the areas of the rectangles.
area1 = length1 * width1
area2 = length2 * width2

#Determine which has the greater area.
if area1 > area2:
    print('R1 is larger than R2.')
elif area2 > area1:
    print('R2 is larger than R1.')
else:
    print('R1 and R2 are equal in area')
