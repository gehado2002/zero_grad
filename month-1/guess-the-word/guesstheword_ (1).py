colors = ["red", "blue", "yellow", "green","black", "white"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
programming_languages = ["Python", "javaScript", "java", "PHP","Swift"]

def show_categories_menu():

    print("😊 Welcome to Word Guessing Game! 😊\n")

    print("""the categories :
    🌈colors    📅days    🐍programming_languages

    press 1 for colors
    press 2 for days
    press 3 for programming languages""")

import random
def choose_category():
    while True:
        try:
            choosen_category=int(input())
            if choosen_category ==1:
                return random.choice(colors).lower()

                break
            elif choosen_category ==2:
                return random.choice(days).lower()
                break
            elif choosen_category ==3:
                return random.choice(programming_languages).lower()
                break
            else :
                print("❌invalid ")
        except ValueError:
            print("⚠️ Please enter a number.")

def play_guessing_game(random_word):
    guessed_letters = []
    trials=5
    print(f"\n🔡 The hidden word has {len(random_word)} letters.")
    while True:
        guessing_letter = input("Guess the letter: ")

        if not guessing_letter.isalpha() or len(guessing_letter) != 1:
            print("🔠 Please enter a single alphabet letter.")
            continue

        if guessing_letter in guessed_letters:
            print("⛔ You already guessed that letter.")
            continue

        guessed_letters.append(guessing_letter)

        if guessing_letter in random_word:
            print('✅ Correct!\n💪 Keep going!')
        else:
            trials -= 1
            print(f'🥴 Incorrect! You have {trials} trials left.')


        display_incomplete_word = ''
        for letter in random_word:
            if letter in guessed_letters:
                display_incomplete_word += letter
            else:
                display_incomplete_word += '_ '

        print(f"Current word: {display_incomplete_word}")

        if '_' not in display_incomplete_word:
            print("🎉 You guessed the word!")
            break
        if trials == 0:
            print(f"💥 Game Over! The word was: {random_word}")
            break

def ask_play_again():
    try_again = input('Play again? "y/n": ').lower()
    print("*"*30,"\n")
    if try_again == 'y':
        return True
    else:
        print('Goodbye 👋')
        return False

while True:
    show_categories_menu()
    selected_word= choose_category()
    play_guessing_game(selected_word)

    if not ask_play_again():
        break

