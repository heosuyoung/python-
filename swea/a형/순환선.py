'''
(A+B)^2 + (C+D)^2 으로 계싼

2개의 직통 노선은 서로 교차 x
A에서 B를 이었는데 c는 a보다 커야하고 d는 b보다 커야함
(2개의 직통 노선은 서로 교차x)

B=A-1이면 안됨 D는 C-1이면 안됨
(인접한 두역을 연결하는 직통 노선xx)

도착지가 2개의 인접한선 or 출발지가 2개의 인접한 선이면 안됨
(B=D+1, A=C+1이면 안됨)

1개의 역에 2개의 직통 노선이면 안도미
(A!=C면안됨)


'''

T=int(input())
for _ in range(1,T+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    if
