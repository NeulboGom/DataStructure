pokemons = ['피카츄', '라이츄', '파이리', '꼬부기', '버터플']


def delete_data(idx):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_of_pokemons = len(pokemons)
    pokemons[idx] = None  # 데이터 삭제

    for i in range(idx + 1, len_of_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[len_of_pokemons - 1])


delete_data(1)
print(pokemons)
delete_data(3)
print(pokemons)