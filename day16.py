# Node insertion and Deletion

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self, data):
        self.data = data
        self.link = None


def print_node(start):
    current = start
    if current is None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()


def insert_node(find_data, insert_data):
    global head, current, pre

    if head.data == find_data:  # 첫 번째 노드 삽입
        node = Node(insert_data)
        # node.data = insert_data
        node.link = head
        head = node
        return

    current = head
    while current.link is not None:  # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node(insert_data)
            # node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node(insert_data)  # 마지막 노드 삽입
    # node.data = insert_data
    current.link = node


def delete_node(delete_data):
    global head, current, pre

    if head.data == delete_data:
        current = head
        head = head.link
        del (current)
        print("# 첫 노드가 삭제됨 #")
        return

    current = head
    while current.link is not None:
        pre = current
        current = current.link
        if current.data == delete_data:
            pre.link = current.link
            del (current)
            print("# 중간 노드가 삭제됨 #")
            return

    print("# 삭제할 노드가 없음 #")


def find_node(find_data):
    global head, currnet, pre

    current = head
    if current.data == find_data:
        return current

    while current.link is not None:
        current = current.link
        if current.data == find_data:
            return current

    return Node("nameless")



## 전역 변수 선언 부분 ##
# memory = []
head, current, pre = None, None, None
data_array = ["피카츄", "라이츄", "파이리", "꼬부기", "버터플"]

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = Node(data_array[0])  # 첫 번째 노드
    # node.data = data_array[0]
    head = node
    # memory.append(node)

    for data in data_array[1:]:  # 두 번째 노드부터
        pre = node
        node = Node(data)
        # node.data = data
        pre.link = node
        # memory.append(node)

    print_node(head)

    # insert_node("피카츄", "잠만보")
    # print_node(head)
    #
    # insert_node("꼬부기", "어니부기")
    # print_node(head)
    #
    # insert_node("군린보", "거북왕")
    # print_node(head)
    #
    # delete_node("잠만보")
    # print_node(head)
    #
    # delete_node("어니부기")
    # print_node(head)
    #
    # delete_node("김진희")
    # print_node(head)

    print(find_node("파이리").data)
    print(find_node("박민석").data)
