

li = [30, 41, 52]
itb = iter(li)
while True:
    try:
        x = next(itb)
        print(x)
    except StopIteration:
        break
 
