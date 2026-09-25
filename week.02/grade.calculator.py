total_score = 0
student_count = 0

while True:
    name = input("Enter student name (or q to quit): ")
    
    if name.lower() == 'q':
        break
    
    score = float(input("Enter score: "))
    
    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue
    
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"{name}: {int(score) if score.is_integer() else score} -> {grade}")
    
    total_score += score
    student_count += 1

if student_count > 0:
    average = total_score / student_count
    print(f"Total students: {student_count}")
    print(f"Average score: {average:.2f}")
else:
    print("No students entered.")
