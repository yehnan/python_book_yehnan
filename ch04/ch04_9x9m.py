

result = []
for x in range(2, 9+1):
    for y in range(1, 9+1):
        result.append(str(x) + '*' + str(y) + '=' + str(x*y))

print(result)

####

result = [str(x)+'*'+str(y)+'='+str(x*y) for x in range(2, 9+1) 
                                         for y in range(1, 9+1)]

print(result)
