remember = input() #할머니가 외운 알파벳
time_list = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
           #[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
time_sum = 0
for char in remember:
    time_sum += 1 #1초씩 더 걸린다.
    time_sum += time_list[ord(char)-65]
print(time_sum)