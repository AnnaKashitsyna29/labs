def n1():
    list = [1, 2, 4, 33, 9]
    print('Выберете число')
    x = int(input())
    if x in list:
        print(list, x, 'ого,правильно')
    else:
        print(list, x, 'увы,неправильно')
n1()

def n2():
    a=[]
    b=[1,2,4,9,2,8,5]
    for x in b:
        if b.count(x) > 1:
            if x not in a:
                a.append(x)
    print("n2")
    print('*a')

def n3():
    print("n3")
    day = ('Пн','Вт','Ср','Чт','Пт','Сб','Вс')
    x = int(input('Введите кол-во выходных '))
    for i in day:
        print('Рабочие:', *day[:-x])
        print('Выходные:', *day[-x:])
        break
n3()

def n4():
    print("n4")
    import random
    g1=('Карин','Жужин','Монрав','Курин','Дубчак','Эрин')
    g2 = ('Лапин', 'Аарова', 'Вырова', 'Зукина', 'Петров','Фетров')
    x1=[]
    x2=[]
    x=[]
    x1.append(random.sample(g1,5))
    x2.append(random.sample(g2,5))
    x.extend(*x1)
    x.extend(*x2)
    x=tuple(x)
    print('a', x)
    print('b',g1)
    print('b', g2)
    print('b', x)
    print('c', len(x))
    print('d', *sorted(x))
    print('e', 'Иванов' in x)
    print('e', x.count('Иванов'))
n4()

