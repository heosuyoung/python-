 # t=int(input())
# for _ in range(t):
#     m,n,x,y=list(map(int,input().split()))
#     k=x
#
#     while k<=m*n:
#         if (k-y) % n ==0:
#             break
#
#         else:
#             k+=m
#     if k>m*n:
#         k=-1
#     print(k)

def calender(m,n,x,y):
    k=x
    while k<=m*n:
        if (k-y)%n==0:
            return k
        k+=m
    return -1
t=int(input())
for _ in range(t):
    m,n,x,y=map(int,input().split())
    print(calender(m,n,x,y))
