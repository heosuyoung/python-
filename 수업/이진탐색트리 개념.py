# 1.이진 트리의 특성(2개 이하의 자식노드를 가진다)
# 2.왼쪽 자식 노드의 값은 항상 부모 노드보다 작다
# 3.오른쪽 자식 노드의 값은 항상 부모 노드 보다 크다
#
# 트리에 데이터가 저장되는 과정
# 1.루트노드부터 시작
# 2.삽입할 값과 현재 노드의 값을 비교
#     2-1.현재 노드보다 작으면 왼쪽
#     2-2.현재 노드보다 크면 오른쪽
# 3.자식노드가 그 방향에 없다면(빈자리면) 저장
# 4.자식노드가 그 방향에 있따면 2번과정 다시 반복