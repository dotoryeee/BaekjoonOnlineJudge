count = 0
slice_1, slice_2 = map(int, input().split())
for i in range(slice_1):
    count += 1
count *= slice_2
count -= 1 #최초 초콜릿 조각의 개수를 맞추기 위해서
print(count)