'''
3장의 카드 연속적인 번호 'run'
3장의 카드  동일한 번호 'triple'
6장의 카드가  run과 triple로만 이루어지면 'baby-gin'

baby-gin -> yes 아니면 -> no

6개의 카드로 순열 코드 나열 후 함수 이용하여 앞지리 run or triple찾고 나머지도 run or triple이면
cnt+=1해서 cnt가 2면 return true 아니면 return false
babi-gin
'''

arr=list(map(int,input().split()))
path=[]
visited=[0]*6
is_found_babygin=0
def is_babygin():
    cnt=0
    a,b,c=path[0],path[1],path[2]
    if a==b==c:
        cnt+=1
    elif a==b-1==c-2:
        cnt+=1
    a,b,c=path[3],path[4],path[5]
    if a==b==c:
        cnt+=1
    elif a==b-1==c-2:
        cnt+=1
    return (cnt==2)

def recur(lev):
    global is_found_babygin
    if lev==len(arr):
        if is_babygin():
            is_found_babygin=1
        return

    for i in range(len(arr)):
        if visited[i] ==1:
            continue
        visited[i]=1
        path.append(arr[i])
        recur(lev+1)
        path.pop()
        visited[i]=0 #백트래킹
recur(0)
if is_found_babygin:
    print('YES')
else:
    print('NO')

