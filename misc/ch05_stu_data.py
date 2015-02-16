

# dept is department
name, id, age, dept, scores = range(0, 4+1)
dept_phy = 'physics'
dept_math = 'mathematics'
dept_cs = 'computer science'
# calculus, python, electromagnetism, history
s_cal, s_ph, s_em, s_his = range(0, 3+1)
students = [
    ['Amy Chen', '14001', '21', dept_phy, [90, 82, 95, None]],
    ['John Smith', '14003', '20', dept_math, [92, 82, None, 71]],
    ['Elsa Iceman', '14007', '24', dept_math, [93, 92, None, 73]],
    ['Penny Kuan', '14012', '22', dept_cs, [81, 99, 82, None]]
]
print(students)
print(students[0][name])
print(students[1][id])
print(students[2][age])
print(students[3][dept])
print(students[3][scores])
print(students[3][scores][s_cal])

