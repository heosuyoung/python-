from itertools import permutations
n=int(input())
dice=[1,2,3,4,5,6]
for nums in permutations(dice,n):
    print(list(nums))
