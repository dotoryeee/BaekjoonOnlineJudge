import sys
count, target = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort(reverse=True)
sum = 0
card_count = 0
for i in cards:
    sum += i
    if sum > target and i != cards[-1]:
        sum -= i
    else:
        card_count += 1

    if card_count == 3:
        break
print(sum)