def secondLowest(arr):
    return


students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students = sorted(students, key=lambda student: student[1])
scores = sorted({l[1] for l in students})
scores.remove(min(scores))
secondLowest = min(scores)

for student in sorted(students, key=lambda student: student[0]):
    if student[1] == secondLowest:
        print(student[0])

#for _ in range(int(input())):
    #name = input()
    #score = float(input())
    #students.append([name, score])
