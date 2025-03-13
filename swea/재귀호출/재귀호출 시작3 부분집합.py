arr=['Luffy','Zoro','Sanji']
n=len(arr)
def recur(x):
    for i in range(n):
        if x & (1<<(n-1-i)):
            print(arr[i],end=' ')
    print()

for i in range((1<<n)-1,0,-1):
    recur(i)
print()

#강사님 코드
# path = [''] * 3  # 항상 크기가 3인 리스트 유지
# name = ['Luffy', 'Zoro', 'Sanji']
# arr = ['O', 'X']
#
#
# def print_name():
#     for i in range(3):
#         if path[i] == 'O':
#             print(name[i], end=' ')
#     print()  # 줄바꿈
#
# def dfs(lev):
#     if lev == 3:
#         print_name()
#         return
#
#     for i in range(2):
#         path[lev] = arr[i]  # path 리스트를 항상 lev 위치에 채움
#         dfs(lev + 1)
#
# dfs(0)