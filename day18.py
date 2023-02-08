# Chapter9 Graph

# Self Study 9-2 p336

class Graph():  # 클래스 먼저 만들기
    def __init__(self, size):
        self.SIZE = size  # 행렬의 크기 = size * size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]  # 그래프의 초기상태(Adjacency Matrix) 생성
        # 하나의 행 [0,0,0,0]   #[0,0,0,0]이 4개가 됨


## 전역 변수 선언 부분 ##

G1 = None
stack = []  # append() as push
visited_vertex = []

## 메인 코드 부분 ##

G1 = Graph(9)
G1.graph[0][1] = G1.graph[0][2] = G1.graph[0][4] = 1
G1.graph[1][0] = G1.graph[1][2] = G1.graph[1][3] = 1
G1.graph[2][0] = G1.graph[2][1] = G1.graph[2][3] = G1.graph[2][5] = G1.graph[2][4] = 1
G1.graph[3][1] = G1.graph[3][2] = 1
G1.graph[4][0] = G1.graph[4][2] = G1.graph[4][6] = G1.graph[4][7] = 1
G1.graph[5][2] = 1
G1.graph[6][4] = G1.graph[6][8] = 1
G1.graph[7][4] = G1.graph[7][8] = 1
G1.graph[8][7] = G1.graph[8][6] = 1



current = 0  # 시작 정점(A)
stack.append(current)
visited_vertex.append(current)


def append_ver(g_var):
    while len(stack) != 0:
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
            stack.append(current)
            visited_vertex.append(current)
        else:                  # 다음에 방문할 vertex가 없을 경우 stack에서 하나씩 빼는 과정
            current = stack.pop()   # A까지 사라지지 않는 한, len(stack)이 0이 아니기 때문에 while문 반복


def print_graph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(visited_vertex[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(visited_vertex[row], end=' ')
        for col in range(g.SIZE):
            print(g.graph[row][col], end=' ')
        print()
    print()


print("## G1 무방향 그래프 ##")
for hang in range(G1.SIZE):
    for yeol in range(G1.SIZE):
        print(G1.graph[hang][yeol], end=' ')
    print()


append_ver(G1)
print(stack)
print(visited_vertex)
print("방문 순서 -->", end=' ')
for i in visited_vertex:
    print(chr(ord('A') + i), end=' ')


