#순서대로 찾되 찾으면 0로 만들어 버리고 다음 숫자를 찾는 형식으로
#하면 될듯하다
#해당 배열을 튜플로 중복되는 거 없게 값을 배열에 넣음
#그러면 해당 배열 숫자를 구하는 식으로, 구하면 그 숫자를 해당 배열에서 빼고
#arr에서는 -1로 바꿈 그리고 해당 배열을 다 뺄때까지 반복
'''
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
    #apple=sorted(list(tuple(apple))) #생각해보니 순서대로 값이 나오므로 중복된 값은 나올리가 없음 걍 sort써도 될듯
    apple.sort()
    x,y,dir=0,0,0 #시작값

    for num,apple_x,apple_y in apple: #사과 위치 뽑기
        q=deque()
        visited=[[[False] *4 for _ in range(n)] for _ in range(n)]
        q.append((x,y,dir,0)) #시작위치,방향,횟수 넣음
        visited[x][y][dir] = True

        min_turn = float('inf')

        while q:
            current_x,current_y,current_dir,turn=q.popleft()
            #q에서 아까 넣은거 뽑고
            if (current_x,current_y) == (apple_x,apple_y): #사과에 도달하면
                if turn< min_turn:
                    min_turn=turn #최솟값 저장
                    final_dir=current_dir #현재방향 저장, 저장안하면 우회전 돌아가는 거 때문에 값달라짐
                continue
            # 전진 가능하면 전진하고, 전진 안되면 우회전 시도
            nx,ny=current_x+dx[current_dir],current_y+dy[current_dir] #현재 방향에서 다음 칸으로 전진하고
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny][current_dir]: #이게 n범위 안에 들어가고 방문하지않았다면
                visited[nx][ny][current_dir] = True #이거를 방문처리하고
                q.appendleft((nx, ny, current_dir, turn)) #q에 넣음으로서 계속 전진

            current_dir = (current_dir + 1) % 4 #우하좌상에서 +1 %4를하면 우회전으로 돌아가는 거
            if not visited[current_x][current_y][current_dir]:
                visited[current_x][current_y][current_dir] = True
                q.append((current_x, current_y, current_dir, turn + 1))

        cnt += min_turn
        x,y,dir = apple_x,apple_y,final_dir #사과 먹으면 현재 위치와 방향을 기준으로 다음 사과 찾아 떠남


    print(f'#{_} {cnt}')

'''
from collections import deque

# 방향: 우(0), 하(1), 좌(2), 상(3)
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 사과 위치 및 번호 저장
    apples = []
    for y in range(n):
        for x in range(n):
            if arr[y][x] != 0:
                apples.append((arr[y][x], y, x))
    apples.sort()

    y, x, dir = 0, 0, 0  # 시작 위치 및 방향
    total_turns = 0

    for _, ay, ax in apples:
        visited = [[[False] * 4 for _ in range(n)] for _ in range(n)] #방향때문에 *4
        q = deque([(y, x, dir, 0)])
        visited[y][x][dir] = True
        found = False

        while q and not found:
            cy, cx, cd, turns = q.popleft()

            # 도착 시
            if (cy, cx) == (ay, ax): #현재 y,x가 사과 y,x에 도착한다면
                total_turns += turns
                y, x, dir = cy, cx, cd
                found = True
                break

            # 전진
            ny, nx = cy + dy[cd], cx + dx[cd]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx][cd]:
                visited[ny][nx][cd] = True
                q.appendleft((ny, nx, cd, turns))  # 전진은 우선

            # 우회전
            nd = (cd + 1) % 4
            if not visited[cy][cx][nd]:
                visited[cy][cx][nd] = True
                q.append((cy, cx, nd, turns + 1))

    print(f'#{tc} {total_turns}')
