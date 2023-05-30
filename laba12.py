from tkinter import*
def n1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name}\nТип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print("Ресторан открыт!")

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = []

        def print_flavors(self):
            print("Список вкусов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor.title())

    my_ice_cream_stand = IceCreamStand("Мороженное на углу", "Кафе мороженого")

    my_ice_cream_stand.flavors = ["Ваниль", "Шоколад", "Клубника", "Лимон"]

    my_ice_cream_stand.describe_restaurant()
    my_ice_cream_stand.print_flavors()

n1()

def n2():
    flavors = ["ванильное", "шоколадное", "клубничное", "лимонное"]
    vkys = {"Мягкое": flavors, "Стаканчик": flavors, "На палочке": flavors}
    class icecream:
        def __init__(self, name, type, flavors, time, location):
            self.name = name
            self.type = type
            self.flavors = flavors
            self.time = time
            self.location = location


        def disp_flavors(self):
            print("Вкусы мороженного:")
            for flavor in self.flavors:
                print(f"Мороженое {flavor}")

        def disp_location(self):
            print(f'{self.name} - {self.location}:  центр города')

        def disp_time(self):
            print(f'{self.name} - {self.time}: работает с 10:00 до 21:00')

        def add_flavor(self):
            kolvo = input("Сколько вкусов добавить? ")
            while int(kolvo) > 0:
                n = input("Введите мороженое: ")
                flavors.append(n)
                kolvo = int(kolvo) - 1

        def del_vkus(self, ):
            kolvo = input("Сколько вкусов убрать? ")
            while int(kolvo) > 0:
                n = input("Введите мороженое: ")
                flavors.remove(n)
                kolvo = int(kolvo) - 1

        def check_flavor(self):
            t = (input("Проверить вкус мороженного: ") in flavors)
            if t == True:
                print("В наличии")
            else:
                print("Нет в наличии")

        def stick(self):
            print("У нас есть мороженое на палочке")
            r = input("Хотите ли его? ")
            if r == 'да':
                print("приятного аппетита")

        def soft(self):
            print("У нас есть мягкое мороженое")
            r = input("Хотите ли его? ")
            if r == 'да':
                print('приятного аппетита')

        def cup(self):
            print("У нас мороженое в стаканчике")
            r = input("Хотите ли его? ")
            if r == 'да':
                print('приятного аппетита')

    IceCreamStand = icecream("кафе мороженное за углом", "Мороженое",
                             ["шоколадное", "ванильное", "клубничное", "лимонное"], 'Расположение', 'Время')

    IceCreamStand.disp_flavors()
    IceCreamStand.disp_location()
    IceCreamStand.disp_time()
    IceCreamStand.add_flavor()
    IceCreamStand.del_vkus()
    IceCreamStand.check_flavor()
    IceCreamStand.cup()
    IceCreamStand.soft()
    IceCreamStand.stick()
    print ("оставшиеся вкусы:", *flavors)

n2()

def n3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название ресторана: {self.restaurant_name}\nТип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print("Ресторан открыт!")
    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def print_flavors(self):
            print("Список вкусов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor.title())
        def frame(self):
            root = Tk()
            root.geometry("500x230")
            root.title("Мороженое")
            title = Label(font=45)
            for f in self.flavors:
                item = Label(text = f, font=60)
                item. pack()
                title.pack()
            root.mainloop()
    my_ice_cream_stand = IceCreamStand("Мороженное за углом", "Мороженое",
                                      ["вкусы мороженного в кафе - мороженное за углом", "шоколад", "ваниль", "клубника", "лимон"])
    my_ice_cream_stand.frame()
n3()
