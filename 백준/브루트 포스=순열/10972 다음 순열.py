# import sys
# sys.setrecursionlimit(10**6)
#
# n=int(input())
# arr=list(map(int,input().split()))
# result=[]
# total=[]
# visited=[0]*(n+1)
# def dfs():
#     if len(result)==n:
#         #for i in range(len(result)):
#         total.append(result[:])
#         return
#
#     for i in range(1,n+1):
#         if visited[i] != 1:
#             result.append(i)
#             visited[i]=1
#             dfs()
#             result.pop()
#             visited[i]=0
# dfs()
# #print(total)
# found = False
# for i in range(len(total)):
#     if arr==total[i]:
#         found = True
#         if i == len(total)-1:
#             print(-1)
#         else:
#             print(*total[i+1])
#         break
#
# if not found:
#     print(-1)


n=int(input())
arr=list(map(int,input().split()))

find_num=False
for i in range(n-1,0,-1):
    if arr[i-1]<arr[i]: #이렇게 되면 다음 순열이 존재한다는거임 그걸확인
        for j in range(n-1,0,-1): #뒤에서 부터 역순돌려서
            if arr[i-1]<arr[j]: #보다 큰 값이 있으면
                arr[i-1],arr[j]=arr[j],arr[i-1] #바꾸고
                arr=arr[:i]+sorted(arr[i:]) # 그 뒤부터 정렬해서 배열완성
                find_num=True
                break
        if find_num: # 계속 for문 돌아가므로 찾으면 break
            break
if find_num:
    print(*arr)
else:
    print(-1)
