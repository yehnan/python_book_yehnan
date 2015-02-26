

temps = [0, 100, 30.2, 22.5, -15.8, 23.7, -22.5]

def ctof():
    for i in range(len(temps)):
        temps[i] = temps[i] * 9.0 / 5.0 + 32
        
print(temps)
ctof()
print(temps)

####

def ctof(temps):
    result = []
    for i in range(len(temps)):
        result.append(temps[i] * 9.0 / 5.0 + 32)
    return result

temps = [0, 100, 30.2, 22.5, -15.8, 23.7, -22.5]
print(ctof(temps))
print(ctof(temps))

####

def ctof(temps):
    if temps == []:
        return []
    else:
        return [temps[0] * 9.0 / 5.0 + 32] + ctof(temps[1:])

temps = [0, 100, 30.2, 22.5, -15.8, 23.7, -22.5]
print(ctof(temps))


