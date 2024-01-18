import random
def guess_a_number():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")
    answer= random.randint(0,100)
    print(f"the correct number {answer}")
    game_over =False
    #chose level
    level= (input("Choose a difficult level. Type 'easy' or 'hard':")).lower()
    if level== 'easy':
        lives = 10
    else:
        lives = 5
    print(f"You have {lives} attemtps remaining to guess the number")
    #make guess
    while not game_over:
        guess= int(input("Make a guess:"))
        if guess  == answer:
            print("yOU WIN , congrats")
            game_over= True
        elif guess != random:
            lives-= 1
            print(f"You have {lives} attemtps remaining to guess the number")
            if guess < answer:
                print("Too low.")
            elif guess > answer:
                print('Too high')

        if lives ==0:
            game_over= True
            print('You run out of guess. You lose.')
        elif lives>0:
            print("Guess again!")
def play_game():
    while True:
        guess_a_number()
        play_again= input("Do you want to play again ? Y/N")
        if play_again != "y":
            print("Game end!See you next time!")
            break

play_game()