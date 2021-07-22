import random

restart = 'y'

while(restart == 'y'):
    message = """Hello :) ! My name is Computer and I am thinking of a number between 1 and 20.
    Can you guess what number I am thinking of? You get 5 chances to guess correctly.
    If you do that you win, but if you lose all 5 chances you lose! So let's get started.
    All the best!
    """

    print(message)


    n = random.randint(1,20)

    num_chances = 5

    while(num_chances!=0):
        guessed_number = int(input("Enter your guess: "))
        if(guessed_number == n):
            print("Yay! You guessed correctly!")
            break
        elif(guessed_number > n):
            print("Guessed number is greater than original number")
            num_chances -= 1
        else:
            print("Guessed number is lesser than the original number")
            num_chances -= 1

    if num_chances == 0:
        print("I am sorry but you did not guess correctly :( ")

    restart = input("Would you like to play again? Press \'y\' for yes and \'n\' for no: ")
