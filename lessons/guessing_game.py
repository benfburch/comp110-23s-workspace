"""asks user for a number and goes until they get it right"""

SECRET: int = 4 
guess: int = int(input("guess a number! "))
playing: bool = True
number_of_guesses: int = 0

while playing: 
    
    if number_of_guesses == 3:
        playing = False
    if guess == SECRET: 
        print("good job")
        playing = False
    else:
        print("wrong number :(")
        if guess % 2 == 1: #guess is odd
            print("your guess is odd. the answer is even ")
        if guess > SECRET: 
            print("your guess is too high")
        else: #guess < secret
            print("guess too low")

        guess = int(input("guess again: "))