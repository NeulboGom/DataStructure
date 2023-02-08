# Chapter9 Graph

# 트리와 그래프의 차이: 트리는 Cycle이 없다. 그래프는 있다.
# 지하철 노선도, 도로망, 전기회로 연결 상태 등등이 그래프를 활용한 예시

# 무방향 그래프: 간선(엣지)에 방향성이 없는 그래프
# Vertex: 트리의 Node/ 정점
# G1 = {(A,B), (A,C), (A,D), (B,C), (C,D)}
# G2 = {(A,B), (B,D), (D,C)}

# 방향 그래프: Directed Graph
# G1 = {<A,B>, <A,C>, <A,D>, <B,C>, <C,D>}
# G2 = {<A,B>, <B,D>, <D,C>}

# 가중치 그래프(Weight Graph)
# 엣지 위에 숫자로 가중치를 표현


# Graph Traversal - 그래프 순회 // DFS와 BFS가 대표적이다.
# Depth First Search(DFS) - 깊이 우선 탐색 방식 // Stack 자료구조를 사용한다.
# Bredth First Search(BFS) - 너비 우선 탐색 방식 // Queue 자료구조를 사용한다.


# 그래프의 인접 행렬 표현
# 그래프를 코드로 구현할 때는 인접행렬(Adjacncy Matrix)을 사용
# 인접 행렬은 정방형으로 구성된 행렬로 정점이 4개인 그래프는 4X4로 표현 / ex) Vertex가 5개면 5X5
# 출발 -> 도착 있으면 "1"로 생각 // Undirected Graph 경우 출발점과 도착점이 같아서 대각선 "0"들을 기준으로 대칭적
# 다만 Directed Graph의 경우, 출발 도착점이 명확하기 때문에 대칭적이지 않음


# 그래프의 구현

class Graph():  # 클래스 먼저 만들기
    def __init__(self, size):
        self.SIZE = size  # 행렬의 크기 = size * size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]  # 그래프의 초기상태(Adjacency Matrix) 생성
        # 하나의 행 [0,0,0,0]   #[0,0,0,0]이 4개가 됨


G1 = Graph(4)  # 그래프 객체 생성

for i in range(4):
    for j in range(4):
        if i == j:
            continue
        else:
            G1.graph[i][j] = 1

print(G1.graph)

G3 = Graph(4)
G3.graph[0][1] = 1
G3.graph[0][2] = 1
G3.graph[3][0] = 1
G3.graph[3][2] = 1

print("## G3 방향 그래프 ## ")
for row in range(4):
    for col in range(4):
        print(G3.graph[row][col], end=' ')
    print()

G4 = Graph(4)
G4.graph[0][3] = G4.graph[3][0] = 1
G4.graph[1][3] = G4.graph[3][1] = 1
G4.graph[1][2] = G4.graph[2][1] = 1

print(" ## G4 무방향 그래프 ## ")
for hang in range(4):
    for yeol in range(4):
        print(G4.graph[hang][yeol], end=' ')
    print()

# 그래프 개선
# Moon, Solar, Hwi, Tsu = 0, 1, 2, 3
# 요런식으로 만들면 쌍당히 직관적임
# G1.graph[Moon][Solar] = 1  ->  Moon과 Solar가 연결 됐다. 보기 편함 갸꿀


# 행과 열의 주석을 추가하여 출력하기 + 함수로 만들기
g = Graph(6)
char_list = ["A", 'B', 'C', 'D', 'E', 'F']


def print_graph(g):
    print(' ', end=' ')  # 맨 앞에 빈칸 두기
    for v in range(g.SIZE):  # 행 방향 변수 쫙 나열
        print(char_list[v], end=' ')
    print()  # 한 줄 띄고
    for row in range(g.SIZE):  # 일단 변수 나열 + 내부 for 문으로 행렬 출력
        print(char_list[row], end=' ')  # 열 방향으로 변수 쫙 나열
        for col in range(g.SIZE):  # 행렬 출력
            print(g.graph[row][col], end=' ')
        print()
    print()


# 깊이 우선 탐색의 구현
# DFS 구현을 위한 준비:
# 1. stack을 사용해야함
# 2. 코드를 좀 더 간략히 하고자 별도의 top을 사용하지 않고, append()로 push를, pop()으로 팝하는 스택을 사용
# stack이 비어있으면 전부 다 방문한 것으로 간주한다.

G9 = Graph(4)

visited_vertex = []
visited_vertex.append(0)  # A vertex를 방문했을 때
visited_vertex.append(1)  # B vertex를 방문했을 때

if 1 in visited_vertex:
    print("A는 이미 방문함")

for i in visited_vertex:
    print(chr(ord("A") + i), end=' ')  # visted_vertex 내부의 A~요런거를 출력하기 위한 코드
print()

print("=" * 70)
## 전역 변수 선언 부분 ##

G1 = None
stack = []  # append() as push
visited_vertex = []

## 메인 코드 부분 ##

G1 = Graph(4)
G1.graph[0][2] = G1.graph[0][3] = G1.graph[1][2] = 1
G1.graph[2][0] = G1.graph[2][1] = G1.graph[2][3] = 1
G1.graph[3][0] = G1.graph[3][2] = 1

print("## g1 무방향 그래프 ##")
for hang in range(4):
    for yeol in range(4):
        print(G1.graph[hang][yeol], end=' ')
    print()

current = 0  # 시작 정점(A)
stack.append(current)
visited_vertex.append(current)


def append_ver(g_var):
    while len(stack) != 0:
        global current
        ne_xt = None
        for vertex in range(4):
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


append_ver(G1)
print(stack)
print(visited_vertex)
print("방문 순서 -->", end=' ')
for i in visited_vertex:
    print(chr(ord('A') + i), end=' ')
