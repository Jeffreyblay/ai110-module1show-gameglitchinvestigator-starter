# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
Glitchy Guesser is a number-guessing game where the player tries to find a secret number within a limited number of attempts, earning points for guessing quickly.
- [ ] Detail which bugs you found.
The debug panel exposed the secret answer to players, the "Attempts left" count lagged one guess behind, and out-of-range guesses (like 101 on Normal) wrongly got a "Go LOWER" hint instead of being rejected.
- [ ] Explain what fixes you applied.
I removed the debug panel, fixed the attempts-left display to update accurately after each guess, and added range validation so out-of-range numbers show an "Out of range" error for every difficulty.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Player selects "Normal" difficulty (range 1–100) and sees "Attempts left: 8".
2. Player enters 50 → game returns "📈 Go HIGHER!" and the score updates.
3. Player enters 150 → game shows "⛔ Out of range! Enter a number between 1 and 100." instead of a misleading hint.
4. Player enters 75 → game returns "📉 Go LOWER!" and "Attempts left" decreases correctly after each guess.
5. Player enters the secret number → game shows a win message with the final score, and the secret stays hidden until the game ends.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
