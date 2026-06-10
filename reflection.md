# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game showed, with the developer bug, which shows the answer to the guess word, when clicked on.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The number of attempts left were not displayed to inform the player about the attempts left.
  2. When you go beyond the range for each difficulty level, you do not get notified.
  3. The developer bug, which had the answer to the guess word and other additional information, was accessible to the player.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 101 |out of range |Get lower |none |
|click on developer bug |not show on interface |shows on interface |'shows answer to guess number |
| number of attempts count| show number of attempts left | none | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude AI
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I made inquiries about the range values for the difficulty levels. The AI suggested that, when i out of range number is guessed, an error message "Enter a number between 1 and 100" should show. This was a good suggestion and helped address the issue i raised. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
On the other hand, AI further suggested that a rejected guess or out of range guess still counts as an attempt, itd be best to not burn an attempt on invalid/out of range guesses. This was a wrong suggestion, becuase an out of range attempt is still an attempted guess and should be counted as such.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
1. I manually read the code to verify the update from the AI and then run the code for each bug.
2. After addressing and manually validating each bug, i an overall test run.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
With the help of AI i developed simple pytest script to do a unit testing on the logic of the backend. It should the coherent implementation and logic of the backend scripts.

- Did AI help you design or understand any tests? How?
Yes, it helped to develop the unit testing script to test for various logical functions such as parsing above and below ranges, float rejection, etc. It also assisted me to understand what unit testing is.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit redoes the whole page everytime you click, and session state is the memory box that keeps your stuff from getting erased.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
Lean more into vibe coding. It is very helpful with debugging.

- What is one thing you would do differently next time you work with AI on a coding task?
Tailor more of my inquiries to the specific help/assistance i need from the prompt.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It shows how efficient and simple you can leverage on AI to save time and debug errors quickly. 