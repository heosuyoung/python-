'''
3장의 카드 연속적인 번호 'run'
3장의 카드  동일한 번호 'triple'
6장의 카드가  run과 triple로만 이루어지면 'baby-gin'

baby-gin -> yes 아니면 -> no

6개의 카드로 순열 코드 나열 후 함수 이용하여 앞지리 run or triple찾고 나머지도 run or triple이면
cnt+=1해서 cnt가 2면 return true 아니면 return false
babi-gin
'''

path = []

def KFC(x):

    if x==2:
        print(path)
        return
    for i in range(3):
        path.append(i)
        KFC(x + 1)
        path.pop()
KFC(0)
