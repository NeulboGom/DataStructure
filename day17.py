# Chapter8 Binary Tree
# 알고리즘, 코딩테스트 이해하는 데에 중요
# 폴더 같이 하위 폴더가 있는... 나무의 뿌리 같은 모양

# 이진트리의 개념: Tree자료구조는 나무를 거꾸로 뒤집어 놓은 형태 / 루트 - 큰 줄기, 레벨1,2,3,4... 뻗어나가는 뿌리 부분
# 부모, 자식 관계의 노드 / 엣지: 두 노드의 연결선
# leaf node: Binary Tree 중 끝단, 자식이 없는 노드
# 이진 트리: 모든 노드의 자식이 최대 2개인 트리(자식이 2개 이하로 구성)
# Full Binary Tree: 리프 노드까지의 모든 노드의 자식이 2개
# Complete Binary Tree: lear node가 꽉 차있지 않을 때
# Normal Binary Tree: 있다 없다
# Skewed Binary Tree: 모든 노드가 우측 혹은 좌측으로 연결된 트리

# 이진 트리의 생성
# 높이가 2고, 데이터가 6개인 Complete Binary Tree

class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


node1 = TreeNode()
node1.data = "화사"

# 노드2, 노드 레
node2 = TreeNode()
node2.data = "솔라"
node1.left = node2

# 노드3, 노드1 라
node3 = TreeNode()
node3.data = "문별"
node1.right = node3

# 노드2 레, 노드1 레레, 노드4
node4 = TreeNode()
node4.data = "휘인"
node2.left = node4

# 노드5, 노드2 라, 노드1 레라
node5 = TreeNode()
node5.data = "쯔위"
node2.right = node5

# 노드 6, 노드 3 레, 노드1 라레
node6 = TreeNode()
node6.data = "선미"
node3.left = node6


# 노드7, 노드4 라, 노드2 레라, 노드1 레레라
node7 = TreeNode()
node7.data = "다현"
node4.right = node7

# 노드8, 노드6라, 노드3레라, 노드1 라레라
node8 = TreeNode()
node8.data = "사나"
node6.right = node8


print('\t', node1.data, end=' ')
print()
print('  ', node1.left.data, node1.right.data, end=' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end=' ')
print()
print(' ', node1.left.left.right.data, '  ', node1.right.left.right.data)


# 이진트리의 순회
# 순회 종류:
# 순회(Traversal): 이진트리 노드 전체를 한 번씩 방문하는 것
# 전위 순회(Preorder Traversal): 노드 데이터를 먼저 처리 / 현재 노드 데이터 처리 - 왼쪽 서브트리 이동 - 오른쪽 서브트리 이동
# 중위 순회(Inorder Traversal): 데이터를 중간에 처리 / 왼쪽 서브트리 - 현재 노드 데이터 처리 - 오른쪽 서브트리 이동
# 후위 순회(Postorder Traversal): 데이터를 마지막에 처리 / 왼쪽 서브트리 이동 - 오른쪽 서브트리 이동 - 현제 노드 데이터 처리
# 후위 순회가 가장 느리다.

# 전위 순회 과정: 방문 처리 - 왼쪽 - 오른쪽
# 1. 화사 - 처리 / 2. 솔라 - 처리 / 3. 휘인 - 처리 / 4. 왼쪽으로 더 내려가지 못함(None)
# 5. 솔라로 다시 올라감 / 6. 솔라는 처리 됐으니까 오른쪽 아래 go / 7. 쯔위 - 처리 / 8. 더 못 내려감(None)
# 9. back to 솔라 / 10. back to 화사 / 11. 문별로 내려감 - 처리 / 12. 선미 - 처리 / 13. 내려갈 곳 없음(None)

# 중위 순회 과정: 왼쪽 - 방문처리 - 오른쪽
#

# 후위 순회 과정: 왼쪽 - 오른쪽 - 방문
# 1. 화사 지나서 솔라 지나서 휘인 / 2. 휘인 아래에 없으니까 휘인 방문처리 / 3. 솔라로 갔다가 오른쪽, 쯔위 / 4. 쯔위 없으니까 방문 처리
# 5. 솔라로 back 그리고 방문 처리 / 6. 화사로 올라가고 아직 처리 ㄴㄴ / 7. 문별 갔다가 왼쪽 선미로 감 / 8. 선미 아래 없으니까 방문 처리
# 9. 문별로 back하고 오른쪽 확인 / 10. 오른쪽 없으니까 문별 처리 / 11. 화사로 back / 12 화사 처리


# 이진트리 순회 구현

def preorder(node):
    if node is None:
        return
    print(node.data, end='->')
    preorder(node.left)  # 재귀함수를 이용: 큰 문제를 작은걸로 반복해서 풀 때
    preorder(node.right)  # 프랙탈처럼, 작은것 반복..


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')


print("전위순회: ", end=' ')
preorder(node1)
print("끝")

print("중위순회: ", end=' ')
inorder(node1)
print("끝")

print("후위순회: ", end=' ')
postorder(node1)
print("끝")

print("="*70)

# 이진 탐색 트리(Binary Search Tree)의 특징
# 이진 트리 중 활용도가 높은 트리로, 데이터 크기를 기준으로 일정 형태를 구성함
# 좌측은 부모 노드보다 작은 값, 오른쪽은 부모 노드보다 큰 값
# 모든 노드 값은 중복되지 않는다.

# 이진 탐색 트리의 생성

memory = []
root = None

name_array = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

node = TreeNode()
node.data = name_array[0]
root = node
memory.append(node)

# name = "레드벨벳"
# node = TreeNode()
# node.data = name

for name in name_array[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
            break
        else:
            if current.right is None:
                current.right = node
            break

    memory.append(node)

find_name = input("검색할 이름 입력: ")
current = root
while True:
    if find_name == current.data:
        print(f"{find_name}을(를) 찾음")
        break
    elif find_name < current.data:
        if current.left is None:
            print(f"{find_name}을(를) 찾을 수 없음")
            break
        current = current.left
    else:
        if current.right is None:
            print(f"{find_name}을(를) 찾을 수 없음")
            break
        current = current.right
