

def gf():
    n = 0
    while True:
        from_send = yield n
        n += 1 if from_send is None else from_send

g = gf()
print(next(g))
print(g.send(3))
print(g.send(5))
print(next(g))
print(g.send(10))






