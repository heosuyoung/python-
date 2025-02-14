n=int(input())
num=0
if n>=500:
    num += n//500
    n= n%500
if n>=100:
    num += n//100
    n= n%100
if n>=50:
    num += n//50
    n= n%50
if n>=10:
    num += n//10
    n= n%10
print(num)
