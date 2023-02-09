# Chapter10 재귀함수

# 피보나치 수열

count_recursion, count_memoization, count_memorecu = 0, 0, 0


def fibo_recu(n):
    global count_recursion
    count_recursion += 1
    """
    재귀함수를 사용한 피보나치 수열
    :param n:
    :return:
    """
    if n <= 1:
        return n
    else:
        return fibo_recu(n - 1) + fibo_recu(n - 2)


print("피보나치 수 --> 1", end=' ')
for i in range(2, 20):
    print(fibo_recu(i), end=' ')

print()

fibonacci = [1, 1]
for i in range(2, 20):
    ans = fibonacci[i - 2] + fibonacci[i - 1]
    fibonacci.insert(i, ans)

print(fibonacci)


def fibo_iter(n):
    """
    반복문을 사용한 피보나치 수열
    :param n:
    :return:
    """
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
        return r[-1]


# Memoization을 사용한 방법
# 결국 재귀를 사용하는데, 공간을 하나 더 씀


def fibo_memo(n):
    global count_memoization
    count_memoization += 1
    """
    Memoization(DP)을 사용한 피보나치 수열
    :param n:
    :return:
    """
    memo = [0, 1]
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        # ans = fibo_memo(n-1)+fibo_memo(n-2)
        # memo.append(ans)
        return memo[n]


memos = [None for _ in range(40)]  # 전역 리스트
memos[0], memos[1] = 0, 1


def fibo_memo_recu(n):
    global count_memorecu, memos
    count_memorecu += 1
    """
    Memoization(DP)을 사용한 피보나치 수열
    :param n:
    :return:
    """
    if n <= 1:
        return memos[n]

    if memos[n] is not None:  # 저역 메모리 memos에 이전에 계산한 결과 값이 존재하면, 재귀함수를 안 하겠다.
        return memos[n]

    memos[n] = fibo_memo_recu(n - 2) + fibo_memo_recu(n - 1)  # 처음 방문하는 n
    return memos[n]


# for i in range(2, 30):
#     print(f"{i}: {fibo_iter(i)} / ", end=' ')
# print()

for j in range(2, 30):
    print(f"{j} : {fibo_recu(j)}")
print()

for i in range(2, 30):
    print(f"{i}: {fibo_memo(i)} / ", end=' ')
print()

for i in range(2, 30):
    print(f"{i}: {fibo_memo_recu(i)} / ", end=' ')
print()

print(f"재귀 = {count_recursion}, 메모 = {count_memoization}, 재귀메모 = {count_memorecu}")

# 재귀함수는 메모리를 많이 쓰는 대신, 속도가 개선, 빨라짐
