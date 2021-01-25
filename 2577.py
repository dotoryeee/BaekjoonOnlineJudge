gop = 1
for i in range(3):
    num = int(input())
    gop *= num
gop=str(gop)
answer = [0,0,0,0,0,0,0,0,0,0]
for char in gop:
    if char == '0':
        answer[0] += 1
    if char == '1':
        answer[1] += 1
    if char == '2':
        answer[2] += 1
    if char == '3':
        answer[3] += 1
    if char == '4':
        answer[4] += 1
    if char == '5':
        answer[5] += 1
    if char == '6':
        answer[6] += 1
    if char == '7':
        answer[7] += 1
    if char == '8':
        answer[8] += 1
    if char == '9':
        answer[9] += 1
for i in answer:
    print(i)