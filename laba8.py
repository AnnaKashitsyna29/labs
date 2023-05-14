from PIL import Image, ImageDraw, ImageFont

def n1():
    a = Image.open('fin.jpeg')
    b = a.crop((30,20,40,440))
    b.show()
    b.save('b.jpeg')
n1()

def n2():
    otkritki = {
        "День победы":"9мая.jpg", "День России":"деньросс.jpg", "День рождения":"деньрож.jpg"
                }
    t =input("Введите праздник?")
    if t in otkritki:
        image = Image.open(otkritki[t])
        image.show()
    else:
        print("открытки нет")

n2()

def n3():
    from PIL import Image, ImageDraw, ImageFont
    name = input("Введите имя")
    filename = "деньрож.jpg"
    with Image.open(filename) as img:
        img.load()
    font = ImageFont.truetype("cambriab.ttf", 30)
    draw_text = ImageDraw.Draw(img)
    draw_text.text(
        (img.width // 2 - 100, 15),
        name + " поздравляю",
        font=font,
        fill=('black')
    )
    img.show()
    img.save(name + "new.png")
n3()