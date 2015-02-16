

def my_sum(li):
    if li == []:
        return 0
    else:
        return li[0] + my_sum(li[1:])

print(my_sum(list(range(100+1))))
print(my_sum([]))
print(my_sum([1, 2, 3]))

def my_len(li):
    if li == []:
        return 0
    else:
        return 1 + my_len(li[1:])
print(my_len(list(range(100+1))))
print(my_len([]))
print(my_len([1, 2, 3]))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a
def gcd_r(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
for i in range(2, 100, 3):
    for j in range(3, 100, 4):
        if gcd(i, j) != gcd_r(i, j):
            print('error', i, j)
            
def ctof2(temp):
    n = my_len(temp)
    i = 0
    while i < n:       
        temp[i] = temp[i] * 9.0 / 5.0 + 32 
        i += 1
data2 = [-30.2, -22.5, 15.8, 23.7, 35.2] 
ctof2(data2)
data = [-30.2, -22.5, 15.8, 23.7, 35.2]                       
def ctof(li):
    if li == []:
        return []
    else:
        return [li[0]*9.0/5.0+32] + ctof(li[1:])
if ctof(data) != data2:
    print('error')
    print(ctof(data))
    print(data2)
