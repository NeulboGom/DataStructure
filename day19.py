# Chapter10 재귀함수

# 재귀함수의 응용
# 회문 판단하기
# palindrome: 인도인, 별똥별, 스위스, 역삼역 우영우


## 클래스 변수와 함수 선언 부분 ##
def palindrome(string):
    if len(string) <= 1:  # 문자열의 길이가 1개 일 때, 이건 회문이 맞음
        return True

    if string[0] != string[-1]:  # 문자열의 첫 문자와 끝 문자가 다르면 / 회문 아님
        return False

    return palindrome(string[1:len(string) - 1])    # 2번째부터 뒤에서 두 번째 문자열까지 슬라이스 하고 재귀로 넣음
                                                    # 계속 잘라가면서 반복하면서 회문 맞는지 판단


## 전역 변수 선언 부분 ##
palst_list = ["reaver", 'kayak']

## 메인 코드 부분 ##
for i in palst_list:
    print(i, end='-->')
    i = i.lower().replace(' ', '')  # 일단 lower로 모든 문자를 소문자로 / replace로 빈칸을 ''로 없앰
    if palindrome(i):  #
        print('O')
    else:
        print("X")
