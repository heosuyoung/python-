# n,m=map(int,input().split())
# arr=[]
# visited=[0]*(n+1)
# def n_m(x):
#     if x==m: # 자릿수네!
#         print(*arr)
#         return
#
#     for i in range(1,n+1):
#         if visited[i]==1: #이게 몇까지 반복할지
#             continue
#         visited[i]=1
#         arr.append(i)
#         n_m(x+1)
#         arr.pop()
#         visited[i]=0
# n_m(0)

n,m=map(int,input().split())
arr=[]
def n_m():
    if len(arr)==m:
        print(*arr)
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            n_m()
            arr.pop()
n_m()