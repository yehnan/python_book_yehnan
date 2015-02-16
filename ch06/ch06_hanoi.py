

def hanoi(n):
    steps = []
    def sub(n, pfrom, pto, pbuf):
        if n == 1:
            steps.append((pfrom, pto))
        else:
            sub(n-1, pfrom, pbuf, pto)
            steps.append((pfrom, pto))
            sub(n-1, pbuf, pto, pfrom)
    sub(n, 'A', 'C', 'B')
    return steps

steps = hanoi(3)
print(steps)

def simulate_hanoi(n, pfrom, pto, pbuf, steps):
    pillars = {pfrom: list(range(n)), pto: [], pbuf: []}
    for s in steps:
        disk = pillars[s[0]].pop()
        pillars[s[1]].append(disk)
    print(pillars[pfrom])
    print(pillars[pto])
    print(pillars[pbuf])
    if (pillars[pfrom] == [] and
        pillars[pbuf] == [] and
        pillars[pto] == list(range(n))):
        return True
    else:
        return False

print(simulate_hanoi(3, 'A', 'C', 'B', steps))
