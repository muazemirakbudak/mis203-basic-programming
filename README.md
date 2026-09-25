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
