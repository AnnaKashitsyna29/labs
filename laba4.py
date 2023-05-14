def n1():
    try:
        n = int(input('Введите число'))
    except ValueError:
        print("Это не число")
    else:
        if n % 3 == 0:
            print('Делится на 3')
        elif n == 0:
            print('Введен 0')
        elif n % 3 != 0:
            print('Не делится на 3')
n1()

def n2():
    try:
        x = int(input("Введите число"))
        y = 100 / x
    except ValueError:
        print("Это не число")
    except ZeroDivisionError:
        print("Введен 0")
    else:
        print(f"100 : {x} = {y}")

n2()

def n3():
        x = input("Введите дату: ")
        x = x.split(".")
        if int(x[0]) * int(x[1]) == int(x[2][2: 4]):
            print("Дата магическая, ура!")
        else:
            print("Дата не магическая")

n3()

def n4():
    ch = input("Введите номер билета: ")
    x = 0
    y = 0
    if len(ch) % 2 == 0:
        for i in ch[0:int(len(ch) / 2)]:
            x = x + int(i)
        for i in ch[int(len(ch) / 2):int(len(ch)) + 1]:
            y = y + int(i)
        if x == y:
            print("Билет счастливый!")
        else:
            print("Билет не является счастливым!")
    else:
        print("Количество цифр нечётно!")
n4()

