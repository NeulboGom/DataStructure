## 함수 선언 부분 ##
def print_poly(p_x):
    """
    다항식 출력
    :param p_x: 계수를 갖고 있는 list
    :return: 다항식 String
    """
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]  # 계수

        if i > 0 and coef > 0:
            poly_str += "+"
        elif coef == 0:
            term += -1
            continue
        poly_str += f"{coef}x^{term}"
        term -= 1

    return poly_str


def cal_poly(x_value, p_x):
    """
    다항식 계산
    :param x_value: x값
    :param p_x: 다항식의 계수 list
    :return: 다항식 계산의 result
    """
    return_val = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        co_ef = p_x[i]  # 계수
        return_val += co_ef * x_value ** term
        term -= 1

    return return_val


px = [7, -4, 0, 5]  # = 7x^3 -4x^2 +0x^1 +5x^0
if __name__ == "__main__":
    pStr = print_poly(px)
    print(pStr)
    x_val = int(input("X 값-->"))
    pxValue = cal_poly(x_val, px)
    print(pxValue)