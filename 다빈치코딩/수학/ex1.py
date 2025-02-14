# n=int(input())
# result=0
# for i in range(1,n+1):
#     result+=i
# print(result)

# n=int(input())
# cnt=1
# sum=0
# while cnt<=n:
#     sum+=cnt
#     cnt+=1
#
# print(sum)
#
# n=int(input())
# my_sum=sum(range(1,n+1))
# print(my_sum)


# def is_prime(n):
#     for i in range(2,n):
#         if n % i ==0:
#             return False
#     return True
#
# num=int(input())
# result=0
# for i in range(2,num+1):
#     if is_prime(i):
#         result+=1
# print(result)
# arr=[]
#
# def push():
#     for i in range(3):
#         num = int(input())
#         arr.append(num)
#         print(arr)
#
# def stack_pop():
#     for i in range(3):
#         arr.pop()
#         print(arr)
# push()
# stack_pop()

def push(stack,item): #stack에 추가한다 stack을 매개변수로
    stack.append(item)#stack의 데이터가 수정이 되기 떄문에 지역변수

def pop_stack(stack):
    if stack: #스택이 비어있지 않으면
        return stack.pop() #반환값이 있어서 return함
    return None #스택이 비어있으면 None 반환