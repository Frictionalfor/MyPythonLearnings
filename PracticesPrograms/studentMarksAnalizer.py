#This file consists of functions to analyze student marks data

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


students = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    marks = []

    for j in range(3):
        m = int(input(f"Enter marks for subject {j+1}: "))
        marks.append(m)

    avg = sum(marks) / 3
    grade = calculate_grade(avg)

    students[name] = {
        "marks": marks,
        "average": avg,
        "grade": grade
    }

# Display results
print("\n--- Student Report ---")
topper = ""
highest_avg = 0

for name, data in students.items():
    print(f"{name} -> Avg: {data['average']:.2f}, Grade: {data['grade']}")

    if data["average"] > highest_avg:
        highest_avg = data["average"]
        topper = name

print(f"\n Topper: {topper} with average {highest_avg:.2f}")
