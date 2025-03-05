bt=[0, 'A','B','T','R','S','V']
bt+=[0]*100
def dfs(now):

    if bt[now]==0:
        return

    #전위 순회
    dfs(now * 2)  # 왼쪽 자식 노드
    print(bt[now])  # 현재노드
    dfs(now * 2 + 1)  # 오른쪽 자식 노드

    # #중위 순회
    # print(bt[now])  # 현재노드
    #
    # dfs(now * 2)  # 왼쪽 자식 노드
    # dfs(now * 2 + 1)  # 오른쪽 자식 노드
    #
    # #후위 순회
    # dfs(now*2+1) #오른쪽 자식 노드
    # dfs(now*2) #왼쪽 자식 노드
    # print(bt[now]) #현재노드
dfs(1)