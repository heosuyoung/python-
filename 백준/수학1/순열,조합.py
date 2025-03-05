from itertools import permutations #순열
from itertools import combinations #조합
from itertools import product      #중복순열
from itertools import combinations_with_replacement #중복조합
#순열 :중복허용o 뽑힌 순서대로 의미가있다(값이 같더라도 순서가 다르면 다른경우의수)
for i in permutations([1,2,3,4],2):
    print(i,end=' ')
print()
#(1, 2) (1, 3) (1, 4) (2, 1) (2, 3) (2, 4) (3, 1) (3, 2) (3, 4) (4, 1) (4, 2) (4, 3)


#조합 : 중복허용x, 어떤 것을 뽑은지만 중요하게 여김,
for i in combinations([1,2,3,4],2):
    print(i,end=' ')
print()
#1, 2) (1, 3) (1, 4) (2, 3) (2, 4) (3, 4)
#중복순열
for i in product(range(1,4),range(3)):
    print(i,end=' ')            #range를 똑같이 range(3),range(3)
print()                         #이렇게 늘리는거는 repeat 수를 늘리는 거랑 똑같음
                                #ex: range(3),range(3),range(3) == [0,1,2],repeat=3
for i in product([1,2], repeat=4):
    print(i,end=' ')
print()
#중복조합
for i in combinations_with_replacement([1,2,3,4],2):
    print(i,end=' ')

#import math

#순열의 개수 구하기
n=5
r=3
math.perm(n,r)

#조합의 개수 구하기
n=5
r=3
math.comb(n,r)