crimes=[[5,7,9,55],[30,10,6,8]]
peoples=[[1,2,3,4],[5,7,10,15]]

dat=[0]*100
crime=0
people=0
for i in range(2):
    for j in range(4):
        dat[crimes[i][j]]+=1
for i in range(2):
    for j in range(4):
        if dat[peoples[i][j]] >= 1:
            crime +=1
        else:
            people += 1
print(crime,people,end=" ")