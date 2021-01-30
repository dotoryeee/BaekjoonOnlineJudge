alpha_list = []  #[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
for i in range(0, 26):
    alpha_list.append(97+i)

origin = input()

word = []
for char in origin:
    word.append(ord(char))

cursor = 0
for i in char:
    if