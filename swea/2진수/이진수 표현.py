# T=int(input())
# for _ in range(1,T+1):
#     n,m=map(int,input().split())
#     result=''
#     for i in range(n):
#         if m%2==0:
#             result='OFF'
#             break
#         else:
#             result='ON'
#             m=m//2
#     print(f'#{_} {result}')

T=int(input())
for _ in range(1,T+1):
    n,m=map(int,input().split())
    result=''
    for i in range(n):
        if m & 0x1 :
            result='ON'
            m >>= 1

        else:
            result='OFF'
            break
    print(f'#{_} {result}')
