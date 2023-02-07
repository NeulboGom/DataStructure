# 큐의 응용
# if) 데이터가 겁나 많다.. 막 100만개 이러면, 이전 방식으로는 for문이 겁나 돌아야 함... 엄청난 Overhead다.
# 시간 복잡도가 말도 안 될듯...
# 큐를 원형으로 만듬... Overhead가 발생하지 않게
# 원형 큐의 full 기준은, // if (rear+1) % SIZE == front //
# 하나를 빼야만 full 기준을 잡을 수 있다. 수백 수천 수만의 데이터 중 하나면 싸게 먹힌 것
# 만약 하나를 안 빼고 ㄹㅇ full로 하면 front와 rear가 같아서 empty 기준(if front == rear:)과 같음

SIZE = 10
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
front, rear = 0, 0


# 큐 꽉 찼는지 확인하는 함수
def isqueue_full():
    global SIZE, queue, front, rear
    if (rear+1) % SIZE == front:
        return True
    else:
        return False


# 큐 empty 확인 함수
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
    rear = (rear+1) % SIZE
    queue[rear] = data


# 큐 추출 함수
def de_queue(data):
    global SIZE, queue, front, rear
    if isqueue_empty():
        print("큐가 비었습니다.")
        return
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

# 다음에 추출될 요소 확인 
# linear 형태의 큐
'''
def peek():
    global SIZE, queue, front, rear
    if isqueue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front+1]
'''

# Circular 큐
def peek():
    global SIZE, queue, front, rear
    if isqueue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % SIZE]