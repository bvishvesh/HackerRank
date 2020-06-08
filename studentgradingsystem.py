def gradingStudents(grades):
    finalgrades=[]
    for i in range(len(grades)):
        if(grades[i]<38):
            finalgrades.append(grades[i])
        elif((grades[i]+5-grades[i]%5)-grades[i]<3):
            grades[i]=grades[i]+5-grades[i]%5
            finalgrades.append(grades[i])
        else:
            finalgrades.append(grades[i])
    return finalgrades        

grades_count = int(input().strip())
grades = []
for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)
result=gradingStudents(grades)
for _ in range(len(result)):
    print(result[_],sep="\n")
