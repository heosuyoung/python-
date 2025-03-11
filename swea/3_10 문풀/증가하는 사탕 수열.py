# 틀린 풀이
# t=int(input())
# for _ in range(1,t+1):
#     arr=list(map(int,input().split()))
#     result=0
#     for i in range(2,0,-1):
#         a=0
#         if arr[i-1]>=arr[i]:
#             a+=abs(arr[i]-arr[i-1])+1
#             arr[i-1]-=a
#             result+=a
#         else:
#             continue
#     #
#     # if arr[0]>=arr[1] and arr[1]<arr[2]:
#     #     arr[0]+=abs(arr[1]-arr[0])+1
#     #     arr[0]-=a
#     #     result+=a
#
#     for i in range(2):
#         if arr[i]>arr[i+1] or arr[i]<0 or arr[i]==0:
#             result=-1
#             break
#         else:
#             continue
#
#     print(f'#{_} {result}')



