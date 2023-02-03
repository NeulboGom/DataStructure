# 단순 연결 리스트

class Node():
    def __init__(self):
        self.data = None
        self.link = None


node1 = Node()
node1.data = "다현"


node2 = Node()
node2.data = "정연"
node1.link = node2  # node1이 node2의 메모리 번지를 가리키고 연결

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

# print(node1.data, end=" ")
# print(node1.link.data, end=" ")
# print(node1.link.link.data, end=" ")
# print(node1.link.link.link.data, end=" ")
# print(node1.link.link.link.link.data, end=" ")

current = node1
print(current.data, end=" ")
while current.link is not None:     #link연결이 없으면 None 있으면 while문 실행
    current = current.link
    print(current.data, end=" ")

print(" ")
print("="*60)

# 노드 삽입
newNode = Node()
newNode.data = "재남"
newNode.link = node2.link       # 재남이 쯔위(node2.link 정연의 화살표)를 가리킴
node2.link = newNode            # node2.link 정연의 화살표가 재남을 가리킴

current = node1
print(current.data, end=" ")
while current.link is not None:
    current = current.link
    print(current.data, end=" ")

print(" ")
print("="*60)



