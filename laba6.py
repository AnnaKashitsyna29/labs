def n1():
    K={"Russia":"Moscow","Denmark":"Kopengagen","England":"London","Finland":"Helsinki"}
    print("a",K)
    x=input('Введите страну')
    print("b", K[x])
    print("c", sorted(K))
n1()
def n2():
    mkj = {
        1 : ['а','в','е','и','н','о','р','с','т'],
        2 : ['д','к','л','м','п','у'],
        3 : ['б','г','ё','ь','я'],
        4 : ['й','ы'],
        5 : ['ж', 'з', 'х', 'ц', 'ч'],
        8 : ['ш', 'э', 'ю'],
        10 : ['ф', 'щ', 'ъ']
    }
    x=input("Введите слово")
    x=list(x)
    a = 0
    for i in x:
        for k in mkj:
            if i in mkj[k]:
                a+=k
    print('слово стоит', a)
n2()

def z3():
    studies={
        'A' : ['eng','rus','spa'],
        'B': ['eng', 'rus', 'chi'],
        'C': ['eng', 'rus'],
        'D': ['rus', 'chi'],
        'E': ['rus'],
        'F': ['eng', 'spa'],
        'G': ['kz', 'rus'],
        'H': ['eng', 'it'],
        'I': ['eng', 'fr'],
    }
    d = []
    c = 0
    r=[]
    for i in studies:
        for i in studies[i]:
            if i not in d:
                d.append(i)
                c+=1
    for i in studies:
        if 'chi' in studies[i]:
            r.append(i)
        else:
            continue
    print('n3:')
    print(*d)
    print('всего языков:',c)
    print(*(sorted(d)))
    print('знают китайский', *r)
z3()
