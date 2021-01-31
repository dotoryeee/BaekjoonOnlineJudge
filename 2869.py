import sys
import math
data = list(map(int, sys.stdin.readline().split()))
climb = data[0] - data[1]
one_step_before = data[2] - data[0]
print(math.ceil(one_step_before/climb)+1)