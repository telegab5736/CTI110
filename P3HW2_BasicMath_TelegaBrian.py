#CTI-110
#P3HW2-BasicMath
#Brian Telega
#18June2020


#user input first number
num1 = int(input('Enter your first number:'))
num2 = int(input('Enter your second number:'))


print('----------MENU----------')
print('1) Add Number\n2) Multiply Numbers\n3) Subtract Numbers\n4) Exit')
print('-------------------------')

#input menu options
menu = int(input('Choose from the menu:'))

#value  for menu options
if menu == 1:
    menu = num1 + num2
    print(num1+num2)
elif menu == 2:
    menu = num1 * num2
    print(num1*num2)
elif menu == 3:
    menu = num1 - num2
    print(num1-num2)
elif menu == 4:
    menu = exit()
else:
    print('error')

    




               
            





    
