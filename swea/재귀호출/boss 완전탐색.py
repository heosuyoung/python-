from itertools import product

n=int(input())
cnt=0
dice=[1,2,3,4,5,6]

for x in product(dice,repeat=n):
    if sum(x)<=10:
        cnt+=1
print(cnt)
