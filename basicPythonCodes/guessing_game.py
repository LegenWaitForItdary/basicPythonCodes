import random


def get_name():
    name = input('Please enter your name(Enter q for exit): ')
    while not name:
        print('You did not enter a name')
        name = input('Please enter your name(Enter q for exit): ')
    return name


player_name = get_name()
while player_name != 'q':
    print("Hello " + player_name.title() + " let's play a guessing game! what number from 1 to 20 am I thinking of?")
    secret_number = random.randint(1, 20)
    guessed = False
    remaining_guesses = 4
    while not guessed and remaining_guesses != 0:
        print("You have " + str(remaining_guesses) + " remaining guess/es.")
        remaining_guesses -= 1
        guess = input('Please enter your guess: ')
        guess = int(guess)
        if guess > secret_number:
            print("Guess lower.")
        elif guess < secret_number:
            print("Guess higher.")
        else:
            guessed = True
    if guess == secret_number:
        print("Good job you guessed it right! in " + str(4 - remaining_guesses) + " tries.")
    else:
        print("Sorry! the number I was thinking of was " + str(secret_number) + '.')
    player_name = get_name()
