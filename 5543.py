hamburger = []
ade = []
for _ in range(3):
    hamburger.append(int(input()))
for _ in range(2):
    ade.append(int(input()))
print(min(hamburger)+min(ade)-50)