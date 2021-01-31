import sys
count = int(sys.stdin.readline().rstrip())
nums = []
for i in range(count):
    nums.append(int(sys.stdin.readline().rstrip()))
nums.sort()
for i in nums:
    print(i)