import sys
max_score = 0
new_scores = []
new_sum = 0
new_avg = 0

subjects = int(input())
scores = list(map(int, sys.stdin.readline().split()))

#최고점 찾기
for i in scores:
    if i > max_score:
        max_score = i

#최고점 비율 반환
for i in scores:
    new_score = i / max_score * 100
    new_scores.append(new_score)
#평균 계산
for i in new_scores:
    new_sum += i

print(new_sum / len(new_scores))