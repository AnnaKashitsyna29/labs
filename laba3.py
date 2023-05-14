def n1():
    print(' '.join([input('Введите слово') for i in range(int(input('Количество слов')))]))
n1()


def n2():
    print('Введите слово')
    x= []
    while (y:=str(input()))!="Стоп":
        x.append(y)
        print(' '.join(x))
n2()

def n3():
    x=[]
    while(y:=str(input()))!= "Стоп":
        if "ф" in x or "ф" in y:
            print("Ого,это редкое слово")
        else:
            print("Это не очень редкое слово")
n3()

def n4():

    from random import randint
    print("для завершение напишите Стоп")
    while True:
        x=randint(1,100)
        y=randint(1,100)
        print(f"{x}+{y}=",end="")
        result=input()
        if result == "Стоп":
            break
        result=int(result)
        if x+y==result:
            print("Правильно")
        else:
            print("неПравильно")

n4()
