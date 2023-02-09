# Chapter10 재귀함수
import tkinter as tk

## GUI와 재귀를 이용한 예시

memos = [None for _ in range(100)]
memos[0], memos[1] = 0, 1


# Memoization-Recursion을 사용하여 피보나치 수열을 구하는 함수
def fibo_memo_recu(n):
    global memos
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


# 팩토리얼을 구하는 함수
def fact_recu(n):
    if n == 1:
        return 1
    else:
        return n * fact_recu(n - 1)


# 입력받는 함수
def fact_input():
    lbl_results.config(text=f"팩토리얼 계산 출력 결과: {fact_recu(int(int(en_num_input.get())))}")
    # input_number = int(en_num_input.get())  # ~.get()은


# 입력받는 함수
def fibo_input():
    lbl_results.config(text=f"피보나치 계산 출력 결과: {fibo_memo_recu(int(en_num_input.get()))}")
    # input_number = int(en_num_input.get())


win = tk.Tk()  # 윈도우 생성
win.title("Calculator")  # 피보나치, 팩토리얼 계산기
win.geometry("250x100+800+400")  # 가로, 세로 너비 조정  //win.geometry("가로x세로 + x좌표 + y좌표")

en_num_input = tk.Entry()  # 텍스트 입력 상자
lbl_results = tk.Label(text="계산 출력 결과: ")  # 레이블, 계산 결과 출력용
btn_fact = tk.Button(text="팩토리얼", command=fact_input)  # 팩토리얼 버튼, 이벤트 발생
btn_fibo = tk.Button(text="피보나치", command=fibo_input)  # 피보나치 버튼, 이벤트 발생
# 위에 두 개 처럼 command만 하면 함수가 return을 하긴 하는데 오류 발생됨
# 해서 입력받는 함수를 만들고 상황에 따라서

# 레이아웃(grid 또는 place도 사용 가능)
en_num_input.pack()
lbl_results.pack()
btn_fact.pack(fill='x')
btn_fibo.pack(fill='x')

# 창 생성
win.mainloop()
