#Math quiz program
#12JULY2020
#CTI-110P5HW2-Math Quiz
#Brian Telega





#import random numbers
#program displays 2 random numbers between 1-500

import random
def main():
    print('MAIN MENU \n---------------\n 1) Add Random Numbers \n 2) Subtract Random Numbers \n 3) Exit')
    choice = input()
    if choice == '1':
#make loop so quiz continues
        while True:
#generate two numbers, x and y to take random values
            x = random.randint(1,500)
            y = random.randint(1,500)
#Ask question
            print("What is "  , str (x) , " plus "  , str (y) , "?")
#Ask for answer
            answer = int(input('what is your answer?'))
#Check answer
            if answer == (x + y):
                print('Correct!')
#return to the menu
                main()
            else:
                print('Incorrect, The answer is ' , str(x+y))
    if choice == '2':
        #make loop so quiz continues
        while True:
#generate two numbers, x and y to take random values
            x = random.randint(1,500)
            y = random.randint(1,500)
#Ask question
            print("What is "  , str (x) , " minus "  , str (y) , "?")
#Ask for answer
            answer = int(input('what is your answer?'))
#Check answer
            if answer == (x - y):
                print('Correct!')
#return to the menu
                main()
            else:
                print('Incorrect, The answer is ' , str(x-y))
    if choice == '3':
        exit(0)


main()

   





   

    
    
    




    

