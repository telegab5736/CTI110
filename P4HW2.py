#CTI-110
#P4HW2 - BasicMath
#Brian Telega
#25June2020


#ask for user input
num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number:'))

#display menu
print('----------MENU---------')
print('1) Add Numbers \n2) Multiply Numbers \n3) Subtract Numbers \n4) Exit')

#Create control loop
for menu in range(1,5):
    
#User input
    menu = int(input('Enter a number from menu:'))
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
        
    
     

    



 



