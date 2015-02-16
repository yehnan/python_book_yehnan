
def my_sum(numbers, initial=0):
    total = initial
    for x in numbers:
        total += x
    return total

scores0 = [60, 73, 81, 95, 34]
scores1 = [10, 20, 30, 40, 50, 60]
scores2 = [0, 0, 0]
scores3 = []
scores4 = [-3, -5, -6, -7, -1, -2]

print(str(scores0) + ' total is ' + str(my_sum(scores0)))
print(str(scores1) + ' total is ' + str(my_sum(scores1)))
print(str(scores2) + ' total is ' + str(my_sum(scores2)))
print(str(scores3) + ' total is ' + str(my_sum(scores3)))
print(str(scores4) + ' total is ' + str(my_sum(scores4, 100)))
