

d = {'Amy': 45, 'Bob': 50, 'Cathy': 62, 'David': 45,
     'Eason': 63, 'Fred': 78, 'George': 72, 'Helen': 82,
     'Ivan': 100, 'Jason': 98, 'Kevin': 0, 'Laura': 100}

d2 = {v:k for k,v in d.items()}

d3 = {}
for k, v in d.items():
    r = v // 10
    if r not in d3:
        d3[r] = []
    d3[r].append(k)
print(d3)

#### output: ####
# {0: ['Kevin'], 4: ['David', 'Amy'], 5: ['Bob'], 6: ['Cathy', 'Eason'], 
# 7: ['Fred', 'George'], 8: ['Helen'], 9: ['Jason'], 10: ['Ivan', 'Laura']}






