# n=int(input())
# # arr=''
# # for i in range(1,n+1):
# #     arr+=str(i)
# arr=[str(i) for i in range(1,n+1)]
# result=''.join(arr)
# print(len(result))
n = input()
result = 0
for i in range(1,len(n)):
    result+=9*10**(i-1)*i
result +=(int(n)-10**(len(n)-1)+1)*len(n)
print(result)