# 🎮 Guessing Game – Zero Grad Project

A simple Python-based **number guessing game** where the player chooses a difficulty level and tries to guess a hidden number within a limited number of trials.

---

## 📌 Features
✅ 3 Difficulty Levels: **Easy, Intermediate, Hard**  
✅ Random number generation using Python's `random` module  
✅ User-friendly feedback → **Increase / Decrease hints**  
✅ Allows replaying the game without restarting the program  

---

## 🎯 Game Rules
1️⃣ **Choose a game level:**

- 🟢 **Easy** → Numbers 1–10 (**3 trials**)  
- 🟡 **Intermediate** → Numbers 1–100 (**7 trials**)  
- 🔴 **Hard** → Numbers 1–1000 (**15 trials**)  

2️⃣ A **random number** is generated.  

3️⃣ **Guess the number:**
   - ✅ If correct → 🎉 *Congratulations!*  
   - ❌ If wrong → You get hints ("Increase" / "Decrease") until you run out of trials.  

4️⃣ After the game, you can **choose to play again.**

---

## 📸 Example Output
```
Game Levels:
(1) Easy
(2) Intermediate
(3) Hard

Enter the game level: 1
I have a hidden number, guess it: 5
No, Increase!
I have a hidden number, guess it: 7
No, Decrease!
I have a hidden number, guess it: 6
🎉 You got it successfully in 3 trials!
```

## Feel free to **use, modify, and share** this project! 🚀
