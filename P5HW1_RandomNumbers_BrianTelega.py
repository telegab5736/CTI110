#Random number guessing game
#12JULY2020
#CTI-110 P5HW1 - Random Number
#Brian Telega



import random

def main():
    print('MAIN MENU \n---------------\n 1) Play Game \n 2) Exit')
    choice = input()
    if choice == '1':
        random_num()
    if choice == '2':
        exit(0)

def random_num():
    number = random.randrange(1,100)
    guess = int(input('Guess a number between 1 and 100:'))

    while guess != number:
        if guess < number:
            print('You need to guess higher. Try again.')
            guess = int(input('\nGuess a number between 1 and 100:'))
        else: 
            print('You need to guess lower. Try again.')
            guess = int(input('\nGuess a number between 1 and 100:'))

    print('Congrats!! You picked the correct number')
main()



        
main()









