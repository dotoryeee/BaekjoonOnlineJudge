import sys
listen_num, watch_num = map(int, sys.stdin.readline().split())
no_listen = {}
no_watch = {}
for _ in range(listen_num):
    no_listen[sys.stdin.readline().rstrip()] = 1
for _ in range(watch_num):
    no_watch[sys.stdin.readline().rstrip()] = 1
answer = []
for person in no_listen:
    if person in no_watch:
        answer.append(person)
answer.sort()
print(len(answer))
for person in answer:
    print(person)
