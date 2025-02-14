# T=int(input())
# for i in range(T):
#     n=int(input())
#     while n:
#         print(n//25,end=" ")
#         n%=25
#         print(n //10, end=" ")
#         n %= 10
#         print(n // 5, end=" ")
#         n %= 5
#         print(n//1)
#         n%=1

T=int(input())
for _ in range(T):
    money=int(input())
    for i in [25,10,5,1]:
        print(money//i,end=' ')
        money%=i
    print()