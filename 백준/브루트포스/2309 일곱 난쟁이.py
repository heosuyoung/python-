# arr=[]
# for i in range(9):
#     arr.append(int(input()))
# arr.sort()
# sums=sum(arr)
# #print(arr)
#
# for i in range(9):
#     for j in range(i,9):
#         if sums-arr[i]-arr[j]==100:
#             for k in range(9):
#                 if k==i or k==j:
#                     continue
#                 else:
#                     print(arr[k])
#
#             exit()


#combination을 이용하여 9개중 7개를 모든 조합을 뽑아서 가능
# from itertools import combinations
# arr=[]
# for i in range(9):
#     arr.append(int(input()))
# for i in combinations(arr,7):
#     if sum(i)==100:
#         for j in sorted(i):
#             print(j)
#         break

arr=[int(input()) for _ in range(9)]
result=[]
def dfs(x):
    if len(result)==7:
        if sum(result)==100:
            for num in sorted(result):
                print(num)
            exit()
        return
    for i in range(x,9):
        result.append(arr[i])
        dfs(i+1)
        result.pop()
dfs(0)
