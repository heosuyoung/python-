n=int(input())
nums=list(map(int,str(n)))
nums.sort(reverse=True)
for i in nums:
    print(i,end=' ')