graph = {
    'S': {'a': "A"},
    'A': {'a': "B"},
    'B': {'b': "Z"},
    'Z': {'b': "JC"},
    'JC': {'a': "D", 'b': "K"},
    'D': {'b': "G"},
    'G': {'a': "Z"},
    'K': {'a': "M"},
    'M': {'a': "Z"},
}


def main():
    while True:
        try:
            current = graph['S']
            data = input()
            assert bool(data)
            char = None
            for i in data:
                if i in 'ab':
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