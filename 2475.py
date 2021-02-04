import sys
nums = list((map(int, sys.stdin.readline().split())))
ans = []
for i in nums:
    ans.append(pow(i, 2))
print(sum(ans)%10)