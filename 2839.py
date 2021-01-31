def main():
    bag = 0 #봉투 누적 개수
    sugar = int(input())
    while True:
        if sugar % 5 == 0:
            bag += int(sugar / 5)
            break
        elif sugar <= 0:
            bag = -1
            break
        else:
            sugar -= 3
            bag += 1
    print(bag)
main()