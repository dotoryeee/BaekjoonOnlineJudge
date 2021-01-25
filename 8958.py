import sys

number = int(input())
quizzes = []
scores = []
score = 0
bonus_score = 0

for i in range(number):
    new_quiz = sys.stdin.readline().rstrip()
    quizzes.append(new_quiz)

for quiz in quizzes:
    for ox in quiz:
        if ox == 'O':
            score += 1
            score += bonus_score
            bonus_score += 1
        else:
            bonus_score = 0
    scores.append(score)
    score = 0
    bonus_score = 0

for i in scores:
    print(i)