graph = {
    'S': {'g': "A"},
    'A': {'h': "Z"},
    'Z': {'h': "JC"},
    'JC': {'g': "D", 'h': "K"},
    'D': {'h': "G"},
    'G': {'g': "H"},
    'H': {'g': "Z"},
    'K': {'g': "M"},
    'M': {'g': "N"},
    'N': {'h': "Z"},
}


def main():
    while True:
        try:
            current = graph['S']
            data = input()
            assert bool(data)
            char = None
            for i in data:
                if i in 'gh':
                    current = graph[(char := current[i])]
                    # print(char, end=' ')
                else:
                    raise ValueError()
            print('Цепочка проходит' if char == 'Z' else 'Не достигнут конечный пункт')
        except KeyError:
            print('Нет перехода')
        except AssertionError:
            print('Введена пустая строка')
        except ValueError:
            print('Введен некорректный символ')


if __name__ == '__main__':
    main()