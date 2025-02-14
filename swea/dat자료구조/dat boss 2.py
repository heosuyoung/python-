dat=[0]*5001
T=int(input())
for _ in range(T):
    n = int(input())
    for i in range(n):
        ai,bi=map(int,input().split())
        for j in range(ai,bi+1):
            dat[j]+=1
p=int(input())
arr=[]
for i in range(p):
    arr.append(dat[int(input())])
print(f'#{T} {arr}')