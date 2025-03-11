arr=[]
arr.append(['A','B','T'])
arr.append('')
arr.append(['R','S'])
#print(arr[0][1])
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i].pop(),end='')
    print()