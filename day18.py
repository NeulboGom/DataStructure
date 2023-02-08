# Chapter9 Graph

# 그래프의 응용 - 최소 비용으로 자전거 도로 연결
# 가중치 그래프에서 신장트리 중 합계가 최소인 것
# 구현하는 방법은 프림(Prim) 알고리즘, 크루스컬(Kruskal) 알고리즘이 있음
# 일단 가중치를 오름차순으로 정렬
# 만약 Cycle이 만들어지면 제거
# 간선은 연결 됐다 아니다 뜻으로 '1'과 '0'을 입력했고
# 가중치는 '1'과 '0' 대신 가중치 숫자를 입력

from operator import itemgetter

class Graph():  # 클래스 먼저 만들기
    def __init__(self, size):
        self.SIZE = size  # 행렬의 크기 = size * size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]  # 그래프의 초기상태(Adjacency Matrix) 생성
        # 하나의 행 [0,0,0,0]   #[0,0,0,0]이 4개가 됨


G1 = None
place_array = ["춘천", '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5

G1 = Graph(6)
G1.graph[춘천][서울] = 10
G1.graph[춘천][속초] = 15

G1.graph[서울][춘천] = 10
G1.graph[서울][속초] = 40
G1.graph[서울][대전] = 11
G1.graph[서울][광주] = 50

G1.graph[속초][춘천] = 15
G1.graph[속초][서울] = 40
G1.graph[속초][대전] = 12

G1.graph[대전][서울] = 11
G1.graph[대전][속초] = 12
G1.graph[대전][광주] = 20
G1.graph[대전][부산] = 30

G1.graph[광주][서울] = 50
G1.graph[광주][대전] = 20
G1.graph[광주][부산] = 25

G1.graph[부산][대전] = 30
G1.graph[부산][광주] = 25

visited_vertex = []
stack= []
current = 0  # 시작 정점(A)
stack.append(current)   #en_queue
visited_vertex.append(current)


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
        else:  # 다음에 방문할 vertex가 없을 경우 stack에서 하나씩 빼는 과정
            current = stack.pop()  # 오버헤드 발생 // 큐처럼 first in first out // O(n)
            # current = queue.popleft()   # O(1)


def find_vertex(g, ver):
    global stack, visited_vertex, current
    append_ver(g)
    if ver in visited_vertex:
        return True
    else:
        return False


edge_array = []
for i in range(G1.SIZE):
    for k in range(G1.SIZE):
        if G1.graph[i][k] != 0:
            edge_array.append([G1.graph[i][k], i, k])

print(edge_array)

edge_array = sorted(edge_array, key=itemgetter(0), reverse=True)

new_array = []
for i in range(0,len(edge_array), 2):
    new_array.append(edge_array[i])


idx = 0
while len(new_array) > G1.SIZE - 1:
    start = new_array[idx][1]
    end = new_array[idx][2]
    save_cost = new_array[idx][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    start_yn = find_vertex(G1, start)
    end_yn = find_vertex(G1, end)

    if start_yn and end_yn:
        del new_array[idx]
    else:
        G1.graph[start][end] = save_cost
        G1.graph[end][start] = save_cost
        idx += 1


print("## 최소 비용의 자전거 연결도 ##")
print_graph(G1)
