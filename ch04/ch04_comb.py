

li0 = ['a', 'b', 'c']
li1 = ['.jpg', '.png', '.bmp']
result = []
for x in li0:
    if x != 'a':
        for y in li1:
            if y != '.jpg':
                result.append(x + y)

print(result)

####

result = [x+y for x in li0 if x != 'a' for y in li1 if y != '.jpg']

print(result)
