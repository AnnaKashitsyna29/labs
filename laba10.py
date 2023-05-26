import json
def get_json_string(path: str):
    json_file = open(path, 'r')
    return json_file.read()

products = json.loads(get_json_string("C:\\Users\\Анна\\Desktop\\laba10\\products.json"))
for product in products['products']:
    print(f'Название: {product["name"]}')
    print(f'Цена: {str(product["price"])}')
    print(f'Вес: {str(product["weight"])}')
    print(f'{"Нет в наличии" if product["available"] else "В наличии"} \n')

def n2():
    import json
    with open("products.json", "r") as file:
        exists_data = json.load(file)
    print('Введите данные в виде: Название,Цена,Вес,В наличии')
    new_data = input().split(',')
    exists_data['products'].append(
        dict(
            name=new_data[0],
            price=new_data[1],
            weight=new_data[2],
            available=bool(new_data[3])
        )
    )
    with open('products.json', 'w') as file:
        json.dump(exists_data, file)

    for i in exists_data['products']:
        print(
            f'Название: {i["name"]}\n'
            f'Цена: {i["price"]}\n'
            f'Вес: {i["weight"]}\n'
            f'{"В наличии" if i["available"] else "Нет в наличии"}\n'
        )
n2()

def n3():
    import csv
    with open('en-ru.txt', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter='-')
        result = sorted(
            [row[::-1] for row in reader],
            key=lambda word: word[0]
        )

    with open('ru-en.txt', 'w', encoding='utf-8') as file_output:
        writer = csv.writer(file_output, delimiter='-')
        [writer.writerow(data) for data in result]
n3()
