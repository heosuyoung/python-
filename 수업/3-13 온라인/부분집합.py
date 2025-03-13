arr=['A','B','C']
n=len(arr)

def get_sub(tar):
    print(f'target = {tar}',end=' / ')
    for i in range(n):
        #왜 0x1 이냐?
        #-> 비트 연산임을 명시하는 권장하는 방법
        if (tar>>i) & 0x1: #각 자리의 원소가 포함되어 있나요?
            print(arr[i],end='')
        #tar>>=1

#전체 부분집합을 확인해야한다.
for target in range(1<<n):
    get_sub(target)
    print()