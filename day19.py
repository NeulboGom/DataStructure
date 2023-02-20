# Chapter12 Sort Advanced
import random


# Quick Sort 퀵 정렬 p433
# 최선: nlog(n) (variation is n) / 평균: nlog(n) / 최악: n**2 / 메모리: 뭐라는겨
# 안정: 일반적인 제자리 정렬은 안정적이지 못하다. 안정판이 존재한다. / 방식: 파티셔닝

# Merge Sort: 파티션을 나누고 합치는 것을 반복 - Divide and Conquer - 가르고 정복(?)한다...

# 퀵 정렬:
# 먼저 기준(pivot)을 하나 뽑은 후, 기준보다 작은 그룹과 큰 그룹을 나누어 다시 각 그룹으로 정렬하는 방법
# 이 떄 나눈 그룹을 다시 정렬하고자 재귀 호출을 하고, 각 그룹의 정렬이 완료되면 합치는 방식을 사용한다.
# 기준(pivot): 어떤 것을 선정해도 상관은 없지만, 일반적으로 중간에 위치한 데이터를 선정한다.

########## 퀵 정렬의 간단 구현 #############
## 전역 변수 선언 부분 ##
count = 0


######### 퀵 정렬 오름차순 ##########
## 클래스와 함수 선언 부분 ##
def quick_sort(ls):
    global count
    count += 1
    n = len(ls)  # 리스트의 길이는 n
    if n <= 1:  # 정렬할 리스트가 하나면 정렬할 필요 없음
        return ls

    pivot = ls[n // 2]  # 리스트의 중간에 위치한 값을 pivot으로 설정 / 나중에 들어올 리스트들의 pivot
    left_ls, right_ls = [], []  # 좌측, 우측 요소를 저장할 빈 리스트 생성

    for number in ls:
        if number < pivot:  # pivot보다 작으면 좌측에 저장
            left_ls.append(number)
        elif number > pivot:  # pivot보다 크면 우측에 저장
            right_ls.append(number)

    return quick_sort(left_ls) + [pivot] + quick_sort(right_ls)  # 재귀함수로 요소 하나만 남을 때까지 계속 나누고
    # 결국 정렬해서 중간에 pivot을 두고 다시 합침


# 결국 pivot 값이 잘 잡히면 빠르게 끝나고, 아니면 오래 걸림

check = [random.randint(0, 200) for _ in range(20)]
print(f"정렬 전 --> {check}")

print(f"정렬 후 --> {quick_sort(check)}")
print(f"##{count}회로 정렬 완료")
print("=" * 70)


# Self Study 12-2 p437
########## 퀵정렬 내림차순 ##########

## 클래스와 함수 선언 부분 ##
def quick_sort_rev(ls):
    global count
    count += 1
    n = len(ls)  # 리스트의 길이는 n
    if n <= 1:  # 정렬할 리스트가 하나면 정렬할 필요 없음
        return ls

    pivot = ls[n // 2]  # 리스트의 중간에 위치한 값을 pivot으로 설정 / 나중에 들어올 리스트들의 pivot
    left_ls, right_ls = [], []  # 좌측, 우측 요소를 저장할 빈 리스트 생성

    for number in ls:
        if number > pivot:  # pivot보다 작으면 좌측에 저장
            left_ls.append(number)
        elif number < pivot:  # pivot보다 크면 우측에 저장
            right_ls.append(number)

    return quick_sort_rev(left_ls) + [pivot] + quick_sort_rev(right_ls)  # 재귀함수로 요소 하나만 남을 때까지 계속 나누고
    # 결국 정렬해서 중간에 pivot을 두고 다시 합침


check2 = [random.randint(0, 200) for _ in range(20)]
print(f"정렬 전 --> {check2}")

print(f"정렬 후 --> {quick_sort_rev(check2)}")
print(f"##{count}회로 정렬 완료")
print("=" * 70)


############# 중복 값을 고려한 퀵 정렬 ###########

## 클래스와 함수 선언 부분 ##
def quick_sort_wmid(ls):
    global count
    count += 1
    n = len(ls)  # 리스트의 길이는 n
    if n <= 1:  # 정렬할 리스트가 하나면 정렬할 필요 없음
        return ls

    pivot = ls[n // 2]  # 리스트의 중간에 위치한 값을 pivot으로 설정 / 나중에 들어올 리스트들의 pivot
    left_ls, right_ls, middle_ls = [], [], []  # 좌측, 우측, 중복 요소를 저장할 빈 리스트 생성

    for number in ls:
        if number < pivot:  # pivot보다 작으면 좌측에 저장
            left_ls.append(number)
        elif number > pivot:  # pivot보다 크면 우측에 저장
            right_ls.append(number)
        else:
            middle_ls.append(number)

    return quick_sort_wmid(left_ls) + [pivot] + quick_sort_wmid(right_ls)  # 재귀함수로 요소 하나만 남을 때까지 계속 나누고
    # 결국 정렬해서 중간에 중복값 리스트를 두고 다시 합침


count = 0


# 퀵 정렬 일반 구현 / 리스트 하나로
def quick_sort_advaced(ls, start, end):
    global count
    count += 1
    if end <= start:
        return
    low = start
    high = end
    pivot = ls[(low + high) // 2]
    while low <= high:
        while ls[low] < pivot:
            low += 1
        while ls[high] > pivot:
            high -= 1
        if low <= high:
            ls[low], ls[high] = ls[high], ls[low]
            low, high = low + 1, high - 1
    mid = low
    quick_sort_advaced(ls, start, mid - 1)
    quick_sort_advaced(ls, mid, end)


def quick_sort_advanced_out(ls):
    quick_sort_advaced(ls, 0, len(ls) - 1)


check3 = [random.randint(0, 200) for _ in range(8)]
print(f"정렬 전 --> {check3}")

quick_sort_advanced_out(check3)
print(f"정렬 후 --> {check3}")
print(f"## {count}회로 정렬 완료")
print("=" * 70)
