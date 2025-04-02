#순서대로 찾되 찾으면 0로 만들어 버리고 다음 숫자를 찾는 형식으로
#하면 될듯하다
#해당 배열을 튜플로 중복되는 거 없게 값을 배열에 넣음
#그러면 해당 배열 숫자를 구하는 식으로, 구하면 그 숫자를 해당 배열에서 빼고
#arr에서는 -1로 바꿈 그리고 해당 배열을 다 뺄때까지 반복
from collections import deque
t=int(input())
for _ in range(1,t+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    dx=[0,1,0,-1]
    dy=[1,0,-1,0] #우하좌상 돌림
    apple=[]
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                apple.append((arr[i][j],i,j))
    apple=sorted(list(tuple(apple)))
    x,y,dir=0,0,0

    for num,apple_x,apple_y in apple:
        q=deque()
        visited=[[[False] *4 for _ in range(n)] for _ in range(n)]
        q.append((x,y,dir,0))
        visited[x][y][dir] = True

        min_turn = float('inf')

        while q:
            current_x,current_y,current_dir,turn=q.popleft()

            if (current_x,current_y) == (apple_x,apple_y):
                if turn< min_turn:
                    min_turn=turn
                    final_dir=current_dir
                continue

            nx,ny=current_x+dx[current_dir],current_y+dy[current_dir]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny][current_dir]:
                visited[nx][ny][current_dir] = True
                q.appendleft((nx, ny, current_dir, turn))

            now_dir = (current_dir + 1) % 4
            if not visited[current_x][current_y][now_dir]:
                visited[current_x][current_y][now_dir] = True
                q.append((current_x, current_y, now_dir, turn + 1))

        cnt += min_turn
        x,y = apple_x,apple_y
        dir=final_dir


    print(f'#{_} {cnt}')

