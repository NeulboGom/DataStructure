# p115 응용예제 01

kakao_list = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]


def add_kkt(nm, ct):
    tup_val = (nm, ct)
    for i in range(len(kakao_list) - 1):
        if int(ct) == int(kakao_list[i][1]):
            kakao_list.insert(0, tup_val)
            break
        elif int(ct) > int(kakao_list[i][1]):
            kakao_list.insert(i, tup_val)

    return kakao_list


name = input("추가할 친구-->")
count = input("카톡 횟수-->")
add_kkt(name, count)
print(kakao_list)