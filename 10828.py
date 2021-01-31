import sys

stack = []


def push(num):
    stack.append(num)

def pop():
    try:
        print(stack[-1])
        del stack[len(stack) - 1]
    except:
        print(-1)

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def top():
    try:
        print(stack[-1])
    except:
        print(-1)

count = int(sys.stdin.readline().rstrip())
commands = []
for i in range(count):
    commands.append(sys.stdin.readline().split())

for command in commands:
    if command[0] == 'push':
        push(int(command[1]))
    if command[0] == 'pop':
        pop()
    if command[0] == 'size':
        size()
    if command[0] == 'empty':
        empty()
    if command[0] == 'top':
        top()
