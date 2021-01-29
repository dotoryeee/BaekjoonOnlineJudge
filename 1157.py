import sys

receive = list(sys.stdin.readline().rstrip())

word = []#소문자 데이터
for i in receive:
    word.append(i.lower())
receive.clear()

count = {}#알파벳 카운팅
for i in word:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

final_data = sorted(count, key=lambda x : count[x], reverse=True)
if count[final_data[0]] == count[final_data[1]]:
    print('?')
else:
    print(final_data[0].upper())
