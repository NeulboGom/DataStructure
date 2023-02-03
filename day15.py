def insert_data(idx, pokemon):
    '''
    선형 리스트 idx 위치의 원소 삽입
    :param idx: 순번
    :param pokemon: 포켓몬 종류
    :return: final list
    '''
    if idx < 0 or idx > len(pokemons):
        print("Out of range!")
        return

    pokemons.append(None)  # 빈칸 추가
    # kLen = len(pokemons)  # 배열의 현재 크기

    for i in range(len(pokemons) - 1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "버터플", "야도란"]
    print(pokemons)
    insert_data(2, '파이리')
    print(pokemons)
    insert_data(6, "피죤투")
    print(pokemons)