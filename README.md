# MIS 203 - Basic Programming

## Week 02

- **AI Tool Used:** Gemini
- **Prompt Used:** Ask the user for a student name: Enter student name (or q to quit):
If the user types q, stop the loop with break.
Otherwise, ask for the student's score: Enter score:
If the score is smaller than 0 or bigger than 100, print:
Invalid score. Please enter a number between 0 and 100.
Then go back to the start of the loop. Use continue.
Find the letter grade:
90 – 100: A
80 – 89: B
70 – 79: C
60 – 69: D
0 – 59: F
Print the result like this: Ali: 85 -> B
After the loop ends, print the number of students and the average score, rounded to 2 decimal places:
Total students: 3
Average score: 71.67
If no students were entered, print: No students entered.
- **What did you change?:** I double-checked the loop logic to ensure `break` exits immediately when typing 'q' and `continue` correctly bypasses invalid scores. I also formatted the output to match the assignment requirements.
- **What does break do in your program?:** The `break` statement immediately terminates the infinite `while True` loop as soon as the user enters 'q', allowing the program to proceed to calculating and displaying the final summary.



## Week 03

**AI Tool Used:** Gemini
**Prompt Used:** "Create a Python script named ticket_office.py that sells cinema tickets in a loop, validates inputs (age 0-120, weekday/weekend, student yes/no), applies age/student discounts in specific priority order, and outputs session summary statistics."
**What did you change?** I added error handling with `try-except` for age input so the program doesn't crash on text input, and I used `.strip().lower()` on strings to seamlessly handle trailing spaces and uppercase characters.

### Tests:
1. **Input:** Name: Zeynep, Age: 20, Day: weekday, Student: yes → **Result:** `Zeynep: 140.00 TRY (Student)`
2. **Input (Boundary Test):** Name: Ahmet, Age: 12, Day: weekend, Student: yes → **Result:** `Ahmet: 150.00 TRY (Child)`
3. **Input (Boundary Test):** Name: Elif, Age: 65, Day: weekday, Student: no → **Result:** `Elif: 100.00 TRY (Senior)`

### Why does the order of the rules matter?
The order of the rules matters because Python executes `if/elif` statements sequentially and stops at the first matching condition. If the Student rule came before the Child rule, a 10-year-old student would trigger the Student rule (30% discount) instead of receiving the higher priority Child rule (40% discount).
