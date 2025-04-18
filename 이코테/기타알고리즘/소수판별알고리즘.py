def is_prime_number(x):
    for i in range(2,x):
        if x % i==0:
            return False
    return True
print(is_prime_number(4))
print(is_prime_number(7))


#개선한 알고리즘

import math
def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            return False
    return True
print(is_prime_number(4))
print(is_prime_number(7))

#하나의 수가 소수인지 아닌지 판별