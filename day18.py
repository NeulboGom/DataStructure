#Chapter 10 재귀함수


count = 3


def open_box():
    global count
    print("종이 상자를 엽니다.")
    count -= 1
    if count == 0:
        print("물건을 넣고 반환합니다.")
        return
    open_box()
    print("종이 상자를 닫습니다.")


open_box()