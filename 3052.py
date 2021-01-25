numbers = [] #입력 받을 값
remainders = [] #나머지를 기록
uniqueRemainders = [] #중복값 제거된 remainder
TARGET = 42 #나눗셈 대상값

for i in range(10):
    num = int(input())
    numbers.append(num)

for i in numbers:
    remainder = i % TARGET
    remainders.append(remainder)

for i in remainders:
    if i not in uniqueRemainders:
        uniqueRemainders.append(i)

print(len(uniqueRemainders))