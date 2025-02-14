maps=[[4,5,7,6],[1,5,5,4],[1,1,1,1]]
man=[[5,6,4],[1,5,3]]
dat=[0]*200
for i in range(3):
    for j in range(4):
        dat[maps[i][j]] +=1
for i in range(2):
    for j in range(3):
        print(dat[man[i][j]],end=" ")
    print()