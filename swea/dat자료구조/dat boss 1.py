a=list(map(int,input().split()))
#print(a)
dat=[0]*200
for i in range(len(a)):
    dat[a[i]] +=1

for i in range(len(dat)):
    for j in range(dat[i]):
        print(i,end=" ")