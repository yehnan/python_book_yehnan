

ft = [32, 212, 10, 55, 78, 110, 178]
def ftoc(ft):
    ct = []
    for x in ft:
        ct.append((x - 32) * 5 / 9)
    return ct

ct = ftoc(ft)
print(list(zip(ft, ct)))

####

ft = [32, 212, 10, 55, 78, 110, 178]
ct = [(x - 32) * 5 / 9 for x in ft]
print(list(zip(ft, ct)))

