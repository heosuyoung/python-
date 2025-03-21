l,c=map(int,input().split())
arr=list(input().split())
arr.sort()
visited=[0]*c
result=[]
alphabet=['a','e','i','o','u']
def recursion(x):
    if len(result)==l:
        vowels=sum(1 for char in result if char in alphabet)
        consonants=l-vowels

        if vowels>=1 and consonants>=2:
            print(''.join(result))
            return
    for i in range(x,c):
        if visited[i]!=1:
            visited[i]=1
            result.append(arr[i])
            recursion(i+1)
            result.pop()
            visited[i]=0
recursion(0)
