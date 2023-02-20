# 검색 어떤 집합에서 원하는 것을 찾는 것

# 순차 검색:
# 1. 검색할 집합이 정렬되어 있지 않은 상태일 때
# 2. 처음부터 차례대로 찾아보는 것으로, 쉽지만 비효율적
# 3. 집합의 데이터가 정렬되어 있지 않다면 이 검색 외에 특별한 방법 없음

# 이진 검색:
# 1. 데이터가 정렬되어있다면 이진 검색도 사용 가능
# 2. 순차 검색에 비해 월등히 효율적이라 데이터가 몇 천만개 이상이어도 빠르게 찾아낼 수 있음

#. 트리 검색
# 1. 데이터 검색에는 상당히 효율적이지만, 트리의 삽입 삭제 등에는 부담

# 순차 검색
# 순차 검색의 시간 복잡도:
# 정렬되지 않은 집합의 순차 검색은 데이터의 갯수가 n개라면 시간 복잡도는 O(n)으로 표현됨
# 정렬된 집합의 순차 검색은 검색할 데이터가 없는 경우에도 데이터의 크기가 작다면 앞쪽만 검색한 후, 검색 실패를 효율적으로
# 확인할 수 있음. 하지만 최악의 경우에는 맨 마지막까지 검색할 수 있으므로 시간 복잡도는 O(n)으로 표현해야 한다.
def seq_search(arr, find_data):
    pos = -1
    size = len(arr)
    print("## 비교한 데이터 ==> ", end=' ')
    for i in range(size):
        print(arr[i], end=' ')
        if arr[i] == find_data:
            pos = i
            break
        elif arr[i] > find_data:
            break
    print()
    return pos


data_list = [188, 150, 168, 162, 105, 120, 177, 50]
find_data = 0

find_data = int(input("찾을 값을 입력하세요: "))
print(f"배열 --> {data_list}")
position = seq_search(data_list, find_data)
if position == -1:
    print(f"{find_data} (이)가 없습니다.")
else:
    print(f"{find_data}(은)는 {position} 위치에 있습니다.")



# 이진 검색
def bin_search(data_list, find_data):
    pos = -1
    start = 0
    end = len(data_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if find_data == data_list[mid]:
            return mid
        elif find_data > data_list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return pos

data = [50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
f_data = 162 # 할머니 키


print(f"배열 -> {data}")
position = bin_search(data, f_data)
if position == -1:
    print(f"{f_data} (이)가 없습니다.")
else:
    print(f"{f_data}(은)는 {position} 위치에 있습니다.")


# 이진 검색 알고리즘의 응용
# 색인으로 도서관 책 찾기

from operator import itemgetter

def index_making(ls, idx):
    """

    :param ls:
    :param idx:
    :return:
    """
    before_ls = [(ls[i][idx], i) for i in range(len(ls))]

    after_ls = sorted(before_ls, key = itemgetter(0))
    return after_ls


def book_search(ls, f_data):
    idx = -1
    start = 0
    end = len(ls) - 1

    while start <= end:
        mid = (start + end) // 2
        if f_data == ls[mid][0]:
            return ls[mid][1]
        elif f_data > ls[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return idx


book_ls = [['어린왕자', '쌩떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'], ['신곡', '단테'], ['돈키호테', '세르반테스'],
           ['동물농장', '조지오웰'], ['데미안','헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅']]

title_idx = []
author_idx = []

print(f" # 책장의 도서 --> {book_ls}")
title_idx = index_making(book_ls, 0)
print(f"도서명 색인 표--> {title_idx}")
author_idx = index_making(book_ls, 1)
print(f"작가명 색인표 --> {author_idx}")

find_data = '신곡'
find_position = book_search(title_idx, find_data)
if find_position != -1:
    print(f"{find_data}의 작가는 {book_ls[find_position][1]} 입니다.")
else:
    print(f"{find_data} 책은 없습니다.")


find_data = '괴테'
find_position = book_search(author_idx, find_data)
if find_position != -1:
    print(f"{find_data}의 도서는 {book_ls[find_position][0]} 입니다.")
else:
    print(f"{find_data} 작가는 없습니다.")

