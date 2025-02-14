n,q=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
arr.sort()
for _ in range(q):
    i,j=map(int,input().split())
    if i>n or j>n or i==j or i<0 or j<0:
        print(0)

    elif j>i:
        start = arr[i][1]
        for x in range(i,j):
            if start>=arr[x+1][0]:
                if start<=arr[x+1][1]:
                    start=arr[x+1][1]
        if arr[j][1]==start:
            print(1)
        else:
            print(0)

    elif i>j:
        start = arr[j][1]
        for x in range(j, i):
            if start >= arr[x+1][0]:
                if start <= arr[x+1][1]:
                    start = arr[x+1][1]
        if arr[i][1] == start:
            print(1)
        else:
            print(0)








