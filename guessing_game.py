"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    attempts = 0
    highscore = 1000
    answer = random.randrange(1, 11)
    
    print("""
*----------------------------------------------------------------------*
|                 Welcome to the Number Guessing Game!                 |
*----------------------------------------------------------------------*
    """)    
    
    while True:
        guess = input("I'm thinking of a number between 1 - 10, can you guess what it is? ")
        try:
            guess = int(guess)
            if guess > 10 or guess < 1:
                raise ValueError
        except ValueError:
            print("Sorry, that's not a valid guess. Please guess a number between 1 - 10")
            continue
        else:
            attempts += 1
            if guess == answer:
                print("You got it! It took you {} attempt(s)".format(attempts))
                if attempts < highscore:
                    highscore = attempts
                play_again = input("Would you like to play again? (Y/N) ")
                if play_again.lower() == 'y':
                    answer = random.randrange(1, 11)
                    attempts = 0
                    continue
                print("GAME-OVER, your highscore was {}".format(highscore))
                break
            elif guess < answer:
                print("It's higher")
            elif guess > answer:
                print("It's lower")

# Kick off the program by calling the start_game function.
start_game()