def gradingStudents(grades):
    ans=[]
    for grade in grades:
        if grade<38: 
            ans.append(grade)
        elif grade%5>=3:
            grade=((grade//5)+1)*5
            ans.append(grade)
        else:
            ans.append(grade)
    return ans

print(gradingStudents([84,29,57]))
print(gradingStudents([73,67,38,33]))
