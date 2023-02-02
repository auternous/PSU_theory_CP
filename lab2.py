#8
#Лавов, Логвин 21вп1

#a = input("введите путь: ")
a = '1 2 3 1'
path = a.split(' ')
answer = True
now = 'S'
n = len(path)

if n==0:
    print("пустая строка")
else:
    for i in range(n):
        if now == 'S':
            if path[i] == "3":
                now = "A"
                print(now)
            elif path[i] == "1":
                now = 'B'
                print(now)
            elif path[i] == "2":
                now = 'C'
                print(now)
            else:
                print('недопустимый символ')
                answer = False
        elif now == 'A':
            if path[i] == '3':
                now = "A"
                print(now)
            elif path[i] == '1':
                now = "Z"
                print(now)
            elif path[i] == '2':
                print('нет перехода')
                answer = False
            else:
                print('недопустимый символ')
                answer = False
        elif now == 'B':
            if path[i] == '1':
                now = "B"
                print(now)
            elif path[i] == '2':
                now = "Z"
                print(now)
            elif path[i] == '3':
                print('нет перехода')
                answer = False
            else:
                print('недопустимый символ')
                answer = False
        elif now == 'C':
            if path[i] == '1':
                now = 'Z'
                print(now)
            elif path[i] == '3':
                now = 'C'
                print(now)
            elif path[i] == '2':
                print('нет перехода')
                answer = False
            else:
                print('недопустимый символ')
                answer = False

        elif now == 'Z':
            if path[i] == '1':
                now = "A"
                print(now)
            elif path[i] == '3':
                now = "B"
                print(now)
            elif path[i] == '2':
                now = 'C'
                print(now)
            else:
                print('недопустимый символ')
                answer = False
        if i == (n - 1) and now != "Z":
            print("Не достигнут конечный символ")
            answer = False
            break


print(answer)