students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

student_scores = []
for i in range(len(students)):
    student_scores.append(students[i][1])
student_scores = list(dict.fromkeys(student_scores))
student_scores.sort()
second_lowest = []
for i in range(len(students)):
    if student_scores[1] in students[i]:
        second_lowest.append(students[i][0])
second_lowest.sort()
for students in second_lowest:
    print(students)


