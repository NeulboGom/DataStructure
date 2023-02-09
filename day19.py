# Chapter11 정렬: Sort

import random


# 구글에 파이썬 정렬 알고리즘 검색
# Insertion Sort: 삽입 정렬 405p
# 최선: n / 평균: n**2 / 최악: n**2 / 메모리: 1 / 안정: 예 / 방식: 삽입
# 삽입 정렬도 선택정렬과 마찬가지로 연산 수는 O(n**2)
# 입력 개수가 커질수록 기하급수적으로 비교 횟수(또는 연산 횟수)가 늘어나기에 성능이 좋지 않은 알고리즘

# 기존 데이터 중에서 자신의 위치를 찾아 데이터를 삽입하는 정렬
# 삽입 정렬을 구하기 위해 함수를 정의해야 한다.

# insert할 위치 찾는 함수
def insert_idx(ls, data):
    idx = -1  # 초기값은 없는 위치로
    for i in range(len(ls)):
        if ls[i] > data:
            idx = i
            break
    if idx == -1:  # 큰 값을 못 찾음 == 제일 마지막 위치
        return len(ls)
    else:
        return idx


test_list = []
ins_idx = insert_idx(test_list, 55)
print(f"삽입할 위치 -> {ins_idx}")

test_list = [44, 77, 88]
ins_idx = insert_idx(test_list, 55)
print(f"삽입할 위치 -> {ins_idx}")

test_list = [44, 55, 77, 88]
ins_idx = insert_idx(test_list, 100)
print(f"삽입할 위치 -> {ins_idx}")

# 삽입 정렬 구현
# list의 insert 함수를 사용하여 입력 가능

## 전역 변수 선언 구간 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print(f"정렬 전 ==> {before}")
for i in range(len(before)):
    data = before[i]  # before의 요소들을 data에 하나씩 넣음
    ins_idx = insert_idx(after, data)  # 에프터에 data 하나가 들어갈 위치 확인 / 처음엔 0일걸
    after.insert(ins_idx, data)  # insert로 확인된 자리로 삽입

print(f"정렬 후 ==> {after}")

print('=' * 70)


# p411 Self Study 11-2

## 함수선언 부분 ##
def insert_idx_rev(ls, data):
    idx = -1  # 초기값은 없는 위치로
    for i in range(len(ls)):
        if ls[i] < data:
            idx = i
            break
    if idx == -1:  # 큰 값을 못 찾음 == 제일 마지막 위치
        return len(ls)
    else:
        return idx


## 전역 변수 선언 구간 ##
old = [random.randint(0, 200) for _ in range(10)]
new = []

## 메인 코드 부분 ##
print(f"옛 리스트 -> {old}")
for i in range(len(old)):
    data = old[i]
    ins_idx = insert_idx_rev(new, data)
    new.insert(ins_idx, data)

print(f"새 리스트 -> {new}")
print('=' * 70)


# 여태 방식은 리스트를 두개를 써서 공간이 많이 소요가 돼서
# 리스트 하나로 데이터 정렬하는 쪽으로 효율적이게 바꾸자

## 클래스와 함수 선언 부분 ##
def insertion_sort(ls):
    for end in range(len(ls)):      # for문이 중첩돼서 n**2의 시간을 갖는다.
        for current in range(end, 0, -1):
            if ls[current - 1] > ls[current]:   # 앞의 것과 비교해서, 앞에 것보다 current가 작으면
                ls[current], ls[current - 1] = ls[current - 1], ls[current] # current가 앞으로 가고, 앞에가 current로 온다.
    return ls


## 전역 변수 선언 부분 ##
test = [random.randint(0, 100) for _ in range(8)]
print(f"정렬 전 => {test}")

print(f"정렬 후 => {insertion_sort(test)}")
print("="*70)