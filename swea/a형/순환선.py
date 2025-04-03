#안붙어 있는 것들 result에 추가 한다음 거기서
#result[0]+ result[3] result[1] +result[2]
#하면 될듯 그런데 arr[0]와 arr[-1]은 붙어있음
#거기서 dfs돌려서 최댓값 구하면 될 거 같음
t=int(input())
for _ in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    answer=float('-inf')
    result = []
    dat=[]


    def recur(x):
        global answer
        if len(result) == 4:
            total1=(result[0]+result[3])**2+(result[1]+result[2])**2 #result에 들어 온 놈들 중에
            total2=(result[0]+result[1])**2+(result[2]+result[3])**2 #교차하지않는 방법임 이 중 최댓값
            answer = max(answer, total1,total2)
            return


        for i in range(x,n):
            if (i == 0 and n - 1 in dat) or (i == n - 1 and 0 in dat): #0이랑 배열의 끝이랑 안마주치게
                continue
            if all(abs(i-d) !=1 for d in dat): #안붙어있는 놈들을 조합으로 구현
                result.append(arr[i])
                dat.append(i)
                recur(i+1)
                result.pop()
                dat.pop()
    recur(0)
    print(f'#{_} {answer}')






#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     station = list(map(int, input().split()))
#     max_v = float('-inf')
#     combi1 = []
#     combi2 = []
#     for i in range(N):
#         for j in range(i + 2, N):
#             if j == (i + N - 1) % N: continue
#             combi1.append((i, j))
#
# for s1, e1 in combi1:
#     for s2, e2 in combi1:
#         if s1 < s2 < e1 < e2 or s2 < s1 < e2 < e1: continue
#         if abs(s1 - s2) in [0, 1, N-1] or abs(s1 - e2) in [0, 1, N-1] or abs(e1 - s2) in [0, 1, N-1] or abs(e1 - e2) in [0, 1, N-1]: continue
#
#         okay = (station[s1] + station[e1]) ** 2 + (station[s2] + station[e2]) ** 2
#         max_v = max(max_v, okay)
#
# print(f'#{tc} {max_v}')