A=[4,2,5,3,7,6]
B=[5,3,7]

n=int(input())
flag=1
for i in range(len(B)):
    if A[i+n]!=B[i]:
        flag=0
        break

if flag:
    print('O')
else:
    print('X')