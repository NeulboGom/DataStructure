## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    """
    첫 번째 node가 current를 가리키고, currnet.link가 존재하면
    계속해서 node를 print
    만약 current.link가 없으면
    끝. 그냥 return
    :param start: 1st node(head)
    :return:
    """
    current = start
    if current is None:
        return
    print(current.data, end=' ')
    while current.link is not None:
        current = current.link
        print(current.data, end=' ')
    print()


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["피카츄", "라이츄", "파이리", "꼬부기", "버터플"]

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = Node()  # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:  # 두 번째 이후 노드
        pre = node          # 이전 node를 pre에 백업..
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)
    print(memory)       # 각 node의 메모리 번지수 -> 객체라는 점을 알 수 있음 / memory 리스트 안에 있는 객체임
    print(node.data)
    print(pre.data)


