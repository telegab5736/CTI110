#CTI-110
#P3HW1-Color Mixer
#Brian Telega
#18June2020

#Pseudocode
#input color 1
#input color 2
#four outcomes
#color purple is created
#color orange is created
#color green is created
#error message

#input color from user
color1 = input('Enter color 1:')
color2 = input('Enter color 2:')

#determine color outcome
if (color1 == "red" and color2 == "blue") or (color2 == "red" and color1 == "blue"):
    print('purple')
elif (color1 == "red" and color2 == "yellow") or (color2 == "red" and color1 == "yellow"):
    print('orange')
elif (color1 == "blue" and color2 == "yellow") or (color2 == "blue" and color1 == "yellow"):
    print('green')
else:
    print('error')






