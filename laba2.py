def n1():
    a = input()
    b = input()
    if a == b:
        print("пароль  совпадает")
    else:
        print("пароль не совпадает")
n1()

def n2():
    a = int(input('введите номер места в вагоне'))
    print()
    if a > 36 and a % 2:
        print('боковое место сверху')
    elif a > 36 and a != a % 2:
        print('боковое место сверху')
    elif a < 36 and a % 2:
        print('купе сверху')
    else:
        print('купе сверху')
n2()

def n3():
    # a, b = input(), input()
    if a != 'красный' and a != 'желтый' and a != 'синий':
        print('ошибка цвета ')
    elif b != 'красный' and b != 'желтый' and b != 'синий':
        print('ошибка цвета ')
    elif a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
        print('фиолетовый')
    elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
        print('оранжевый')
    elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
        print('зеленый')
    elif a == 'красный' and b == 'красный':
        print('красный')
    elif a == 'синий' and b == 'синий':
        print('синий')
    elif a == 'желтый' and b == 'желтый':
        print('желтый')
n3()

def n3():
    t = int(input())
    if (t % 4 == 0) and (t % 100 != 0) or (t % 400 == 0):
        print('високосный')
    else:
        print('не високосный')
n3()

def n5():
    print(' '.join([input('Введите слово') for i in range(int(input('Количество слов')))]))
n5()
