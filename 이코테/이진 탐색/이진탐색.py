'''
def binary_search(arr,target,start,end):
    if start>end:
        return None
    mid =(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]>target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr,target,mid+1,end)
n,target=list(map(int,input().split()))
arr=list(map(int,input().split()))
result=binary_search(arr,target,0,n-1)
if result==None:
    print('원소 존재x')
else:
    print(result+1)
'''

def binary_search(arr,target,start,end):
    while start<=end:
        mid=(start+end)//2
        if mid==target:
            return mid
        elif arr[mid]>start:
            end=mid-1
        else:
            start=mid+1
    return None



n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))
result = binary_search(arr, target, 0, n - 1)
if result == None:
    print('원소 존재x')
else:
    print(result + 1)