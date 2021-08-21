def gradingStudents(grades):
    for i in range(0, len(grades)):
        if grades[i] > 37:
            if grades[i] % 5 >=3:
                grades[i] = grades[i] + 5 - (grades[i]%5)
    return grades
