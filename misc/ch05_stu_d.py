

name, id, age, score_math, score_eng = range(0, 4+1)
amy = ['Amy Chen', 14001, 17, 92, 75]
john = ['John Smith', 14009, 18, 81, 84]

print(amy[name])
print(amy[age])
print(john[score_math])
print(john[score_eng])

amy = {
    'name': 'Amy Chen',
    'id': 14001,
    'age': 17,
    'score_math': 92,
    'score_eng': 75,
}
john = {
    'name': 'John Smith',
    'id': 14009,
    'age': 18,
    'score_math': 81,
    'score_eng': 84,
}

print(amy['name'])
print(amy['age'])
print(john['score_math'])
print(john['score_eng'])


