dt=[0,9,4,12,3,6,0,15,0,0,0,0,0,0,13,17]
#dt+=[0]*100
#배열 넘어가면 돌아오게 할려고 사용함

#     if now>len(dt)-1:
#         return 이거 추가함으로써 배열 넘어가면 return되게 수정
def dfs(now):
    if now>len(dt)-1:
        return
    if dt[now]==0:
        return
    dfs(now*2)
    dfs(now*2+1)

    print(dt[now],end=' ')


dfs(1)