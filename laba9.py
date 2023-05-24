import csv
import os
from PIL import Image, ImageFilter
def z1():
    a = ('PNG')
    os.mkdir('new')
    for i in os.listdir():
         if i.endswith(a):
            with Image.open(i) as img:
                img2 = img.filter(ImageFilter.CONTOUR)
            img2.save('new/' + str(i))
z1()
def z2():
    a = ('.jpg', '.PNG')
    os.mkdir('new2')
    for i in os.listdir():
        if i.endswith(a):
            with Image.open(i) as img:
                img2 = img.filter(ImageFilter.CONTOUR)
            img2.save('new2/' + str(i))
z2()
def z3():
    sum = 0
    A = True
    with open("data.csv", "r") as file:
        file = csv.reader(file)
        for i in file:
            if A:
                A = False
            else:
                print(i)
                products = i[0]
                kolvo = i[1]
                cena = i[2]
                print(f"{products} - {kolvo} шт. за ", int(cena) * int(kolvo), " руб.")
                sum += int(kolvo) * int(cena)
    print(f"Итоговая сумма: {sum} руб.")
z3()
