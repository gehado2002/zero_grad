# 🔡 Word Guessing Game – Python Project  

A fun **Python-based word guessing game** 🎮 where players guess letters to reveal a hidden word.  
It includes **multiple categories**, a **limited number of trials**, and **interactive feedback**.

---

## 📌 Features  
✅ Random word selection from categories (Colors 🌈, Days 📅, Programming Languages 🐍)  
✅ Reveals guessed letters while hiding unguessed ones with underscores  
✅ Tracks **incorrect guesses** (max 5 wrong attempts)  
✅ Validates user input to allow **only single alphabet letters**  
✅ Prevents duplicate guesses and gives proper feedback  
✅ Allows players to **play multiple rounds** without restarting the program  

---

## 🎯 How to Play  
1️⃣ Choose a **category**:  
   - 🌈 Colors → Example: red, blue, green  
   - 📅 Days → Example: Monday, Friday  
   - 🐍 Programming Languages → Example: Python, Java  

2️⃣ A random word is selected.  

3️⃣ Guess letters **one at a time**.  
   - ✅ Correct guess → The letter is revealed.  
   - ❌ Incorrect guess → Trials decrease.  

4️⃣ Win 🎉 if you guess the word before running out of trials.  
5️⃣ If you lose 💥, the correct word will be displayed.  
6️⃣ Choose to play again or exit.  

---

## 📸 Example Output
```
😊 Welcome to Word Guessing Game! 😊

the categories :
🌈colors 📅days 🐍programming_languages
Press 1 for colors
Press 2 for days
Press 3 for programming languages
1

🔡 The hidden word has 5 letters.
Guess the letter: e
✅ Correct!
💪 Keep going!
Current word: _ _ ee_
Guess the letter: g
✅ Correct!
💪 Keep going!
Current word: g_ ee_
Guess the letter: r
✅ Correct!
💪 Keep going!
Current word: gree_
Guess the letter: n
✅ Correct!
💪 Keep going!
Current word: green
🎉 You guessed the word!
Play again? "y/n": n

Goodbye 👋
```
