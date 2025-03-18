# n=int(input())
# m=int(input())
# arr=list(map(int,input().split()))
# rimocon=[0,1,2,3,4,5,6,7,8,9]
# for i in range(m):
#     if arr[i] in rimocon:
#         rimocon.remove(arr[i])
# cnt=0
# for i in range(n):
#     if arr[i] in rimocon:
#         rimocon.remove(arr[i])
#         cnt+=1
#     else:
#         while True:
#             if arr[i]-1 in rimocon:
#                 cnt+=1
#                 breal
import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
broken=list(map(int,input().split()))

min_count=abs(100-n) # 100에서 n으로 이동 경우

for nums in range(1000001): # 작은수에서 큰 수로 이동할때 50만
    num=str(nums)            # 큰 수 에서 작은수로 아동할떄 50만해서 100만임
    for i in range (len(num)): #숫자 num의 각 자릿수 확인
        if int(num[i]) in broken:
            break # 해당 숫자가 눌러서 만들 수 없으면 stop
    else: #만들 수 있으면
        min_count=min(min_count, abs(int(num) - n)+len(num))
print(min_count)
