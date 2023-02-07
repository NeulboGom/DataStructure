# 큐 / first in first out // 스택은 last in first out인 것과 대조된다.

# 1. enQueue(인큐): 큐에 데이터를 삽입
# 2. deQueue(디큐): 데이터를 추출
# 3. front(머리): 저장된 데이터 중 첫 번째 데이터
# 4. rear(꼬리): 저장된 데이터 중 마지막 데이터

# stack의 top이 -1이었던 것 처럼 front랑 rear 도 -1로 시작한다.
# 그 뒤로 삽입할 때는 rear가 움직이고, 추출할 때는 front가 움직인다.
# 삽입할 때는 rear += 1, 추출 할 때는 front += 1
# 둘이 같아지면, queue는 비어있음

queue = [None for _ in range(5)]
words = ["화사", "솔라", "문별"]

print(queue)

i = 0
for i in range(3):
    queue[i] = words[i]

print(queue)

print("=" * 30 + "큐 상태" + '=' * 30)
print("[출구] <--", end=" ")
for j in range(0, len(queue)):
    print(queue[j], end=' ')
print('<-- [입구]')
print("=" * 60)

# SIZE = 5
# queue = ['화사', '솔라', '문별', '휘인', '선미']
# front = -1
# rear = 4

print(queue)

# 큐 empty 확인 함수

# 큐 꽉 찼는지 확인하는 함수
'''
def isqueue_full():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False
'''


def isqueue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


# 큐 삽입 함수
def en_queue(data):
    global SIZE, queue, front, rear
    if isqueue_full():
        print("큐가 꽉 찼습니다")
        return
    rear += 1
    queue[rear] = data

'''
# 큐 추출 함수
def de_queue(data):
    global SIZE, queue, front, rear
    if isqueue_empty():
        print("큐가 비었습니다.")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data
'''

print("=" * 60)


# 다만 이렇게 하면  / 화사 / 솔라 / 문별 / 휘인 / 선미 / 형태인데 여기서 앞에께 빠지면서
# /   /   /  문별 / 휘인 / 선미 / 이런 식으로 바뀜 => 저 비어있는 공간이 낭비되고 있다.

# 개선하는 방법:fron -= 1 , rear -= 1

def isqueue_full():
    global SIZE, queue, front, rear
    if rear != SIZE - 1:
        return False
    elif rear == SIZE and front == -1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

#
# SIZE = 5
# queue = [None, None, '문별', '휘인', '선미']
# front = 1
# rear = 4

# print(isqueue_full())
# print(queue)
print("=" * 60)

def de_queue(data):
    global SIZE, queue, front, rear
    if isqueue_empty():
        print("큐가 비었습니다.")
        return
    front += 1
    data = queue[front]
    queue[front] = None
    if queue[front] is not None:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return
    return data


SIZE = 5
queue = ['화사', '솔라', '문별', '휘인', '선미']
front = -1
rear = 4

print(de_queue("화사"))
print(queue)                #de_queue를 개선해보려는 노력데스네
