pokemons = ['피카츄', '라이츄', '파이리', '꼬부기', '버터플']
print(pokemons)

print("=" * 50)


def delete_data(idx):
    '''
    선형 리스트의 idx 번째 뒤로 다 삭제
    :param idx: idx
    :return: [:idx]
    '''
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    # len_of_pokemons = len(pokemons)

    # for i in range(idx - 1, len_of_pokemons):
    #     pokemons[i] = None

    pokemons_list = pokemons[0:idx]
    print(pokemons_list)


delete_data(1)
print("=" * 50)
delete_data(3)

# if __name__ == "__main__":
#     pokemons = ['피카츄', '라이츄', '파이리', '꼬부기', '버터플']
#     print(pokemons)
#     delete_data(1)
#     delete_data(3)