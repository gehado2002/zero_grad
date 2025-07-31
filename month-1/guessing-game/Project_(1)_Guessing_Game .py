def show_levels():
    print(  """Game Levels :\n
      (1) Easy:\n
          * Limits : [1 - 10]\n
          * No. of trials : 3\n
      (2) Intermediate*:\n
          * Limits : [1 - 100]\n
          * No. of trials : 7\n
      (3) Hard :\n
          * Limits : [1 - 1000]\n
          * No. of trials : 15\n """)

"""## Ask the user for the game level"""

def game_level_choice():
    while True :
        game_level =int(input("""Enter the game level :\n
        (1) Easy 	 (2) Intermediate 	 (3) Hard """))
        while game_level not in range (1,4):
            print("invalid")
            break
        else:
            break


    return game_level

"""## Set the game settings according to the game level:

"""

def set_game_settings(game_level):
    if game_level ==1:
        limits=range(1,11)
        n_trials=3

    elif game_level ==2:
        limits=range(1,101)
        n_trials=7

    elif game_level ==3:
        limits=range(1,1001)
        n_trials=15

    return limits, n_trials

## Start Playing


import random

def start_play(limits, n_trials):
    num = random.choice(limits)
    user_trials=1

    while True:

        guess_number=int(input("I have a hidden number, guess it :  "))


        if guess_number == num :
            print(f"You got it successfully in {user_trials} trials")
            break
        elif user_trials<n_trials and guess_number < num :
            print("No, Increase!")
            user_trials+=1
        elif user_trials<n_trials and guess_number > num :
            print("No, Decrease!")
            user_trials+=1

        else :
            print("you lose")
            print(f'the hidden number is {num}')
            break

"""## Let's Play"""

def play():
    show_levels()
    game_level = game_level_choice()
    limits, n_trials = set_game_settings(game_level)
    start_play(limits, n_trials)

def play_again():
    while True :
        again=input("if you want to play again press 'a' ")
        if again =='a':
            play()
        else:
            print("good bye")
            break
    return again

play()
play_again()

