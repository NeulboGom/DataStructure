# Chapter8 Binary Tree

# 이진 탐색 트리에서 데이터 삭제
# 만약 리프 노드와 루트 노드 사이의 노드를 삭제하면, 바로 그 위 노드가 리프노드를 가리킨다(299페이지 참조)
import random


class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


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


## 전역 변수 선언 부분 ##
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인 코드 부분 ##
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    memory.append(node)

delete_name = input("검색할 이름 입력: ")

current = root
parent = None
while True:
    if delete_name == current.data:

        if current.left is None and current.right is None:
            if parent.left == current:
                parent.left = None
            else:
                parent.right = None
            del current

        elif current.left is not None and current.right is None:
            if parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left
            del current

        elif current.left is None and current.right is not None:
            if parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right
            del current

        print(delete_name, '이(가) 삭제됨.')
        break
    elif delete_name < current.data:
        if current.left is None:
            print(delete_name, '이(가) 트리에 없음')
            break
        parent = current
        current = current.left
    else:
        if current.right is None:
            print(delete_name, '이(가) 트리에 없음')
            break
        parent = current
        current = current.right

# 이진 탐색 트리의 응용

book_array = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'],
              ['신곡', '단테'], ['돈키호테', '세브반테스'], ['동물농장', '조지오웰'],
              ['데미안', '헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]
random.shuffle(book_array)

root_book, root_author = None, None

node = TreeNode()
node.data = book_array[0][0]  # 책의 이름
root_book = node

for book in book_array[1:]:
    name = book[0]
    node = TreeNode()
    node.data = name

    current = root_book
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print("책 이름 트리 구성 완료!")

### 작가 이름 트리 ###
node = TreeNode()
node.data = book_array[0][1]
root_author = node
memory.append(node)

for book in book_array[1:]:
    name = book[1]
    node = TreeNode()
    node.data = name

    current = root_author
    while True:
        if name < current.data:
            if current.left is None:
                current.left = node
                break
            current = current.left
        else:
            if current.right is None:
                current.right = node
                break
            current = current.right

    memory.append(node)

print("작가 이름 트리 구성 완료!")

## 책 이름 및 작가 이름 검색 ##
bookOrAuth = int(input('책검색(1), 작가검색(2)-->'))
find_name = input('검색할 책 또는 작가-->')

if bookOrAuth == 1:
    root = root_book
else:
    root = root_author

current = root
while True:
    if find_name == current.data:
        print(find_name, '을(를) 찾음.')
        findYN = True
        break
    elif find_name < current.data:
        if current.left is None:
            print(find_name, '이(가) 목록에 없음')
            break
        current = current.left
    else:
        if current.right is None:
            print(find_name, '이(가) 목록에 없음')
            break
        current = current.right

preorder(root_book)
print()
preorder(root_author)
