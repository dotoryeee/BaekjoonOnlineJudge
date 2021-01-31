import sys
data = list(map(int, sys.stdin.readline().split()))

def main():
    if data[2] <= data[1]:
        print(-1)
    else:
        profit = data[2] - data[1]
        print(int(data[0]/profit)+1)
main()