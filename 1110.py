data = input()
original = int(data)
count = 0
if len(data) == 1:
    data = '0' + data[0]
while True:
    hap = int(data[0]) + int(data[1])
    hap = str(hap)
    if len(hap) == 1:
        nextNum = data[1] + hap
    else:
        nextNum = data[1] + hap[1]
    count += 1
    if int(nextNum) == original:
        break
    data = nextNum
print(count)