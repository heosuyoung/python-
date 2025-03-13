arr=['A','B','C','D','E']
n=3

path=[]
def recur(cnt,start):
    #n명을 뽑으면 종료
    if cnt==n:
        print(*path)
        return
    #5명을 고려
    #for i in range(len(arr)): # (이전에 뽑았던 인덱스 +1,len(arr))을 반복문 돌려야함
    for i in range(start,len(arr)):
        path.append(arr[i])
        #i:i번째를 뽑겠다
        #i+1을 매개변수로 전달: 다음 재귀부터는 i+1부터 고려해라
        recur(cnt+1,i+1)

        path.pop()
recur(0,0)