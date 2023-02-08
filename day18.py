# Chapter9 Graph
from collections import deque


# BFS 너비 우선 탐색
# collection, deque를 이용

class Graph():  # 클래스 먼저 만들기
    def __init__(self, size):
        self.SIZE = size  # 행렬의 크기 = size * size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]  # 그래프의 초기상태(Adjacency Matrix) 생성
        # 하나의 행 [0,0,0,0]   #[0,0,0,0]이 4개가 됨


## 전역 변수 선언 부분 ##

G2 = None
queue = deque([])       # deque as queue
visited_vertex = []

## 메인 코드 부분 ##

G2 = Graph(4)
G2.graph[0][2] = G2.graph[0][3] = G2.graph[1][2] = 1
G2.graph[2][0] = G2.graph[2][1] = G2.graph[2][3] = 1
G2.graph[3][0] = G2.graph[3][2] = 1

current = 0  # 시작 정점(A)
queue.append(current)   #en_queue
visited_vertex.append(current)


def append_ver(g_var):
    while len(queue) != 0:
        global current
        ne_xt = None
        for vertex in range(g_var.SIZE):
            if g_var.graph[current][vertex] == 1:
                if vertex in visited_vertex:  # 방문한 적이 있으면 / 방문 기록에 존재하면
                    pass
                else:
                    ne_xt = vertex  # 아니면 ne_xt에 정점 숫자를 넣음
                    break

        if ne_xt is not None:  # 다음에 연결할 next가 있다면 stack에 하나씩 넣는 과정
            current = ne_xt
            queue.append(current)
            visited_vertex.append(current)
        else:  # 다음에 방문할 vertex가 없을 경우 stack에서 하나씩 빼는 과정
            #current = queue.pop(0)  # 오버헤드 발생 // 큐처럼 first in first out // O(n)
            current = queue.popleft()   # O(1)


def print_graph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(chr(visited_vertex[v]+65), end=' ')
    print()
    for row in range(g.SIZE):
        print(chr(visited_vertex[row]+65), end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end=' ')
        print()
    print()


print("## G1 무방향 그래프 ##")
for hang in range(G2.SIZE):
    for yeol in range(G2.SIZE):
        print(G2.graph[hang][yeol], end=' ')
    print()

append_ver(G2)
print(queue)
print(visited_vertex)
print("방문 순서 -->", end=' ')
for i in visited_vertex:
    print(i, end=' ')
print()

print("방문 순서 -->", end=' ')
for i in visited_vertex:
    print(chr(ord("A") + i), end=' ')
print()

print("="*70)
print_graph(G2)


