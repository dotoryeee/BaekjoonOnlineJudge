def d(number):
    temp = str(number)
    sum = number
    for i in temp:
        sum += int(i)
    return sum

passes = []

for i in range(1, 10000):
   passes.append(d(i))
passes.sort()

for i in range(1, 10000):
    if i in passes:
        pass
    else:
        print(i)