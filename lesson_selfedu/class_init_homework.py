class Money:

    def __init__(self, money):
        self.money = money

    def my_money(self):
        return self.money


my_mon = Money(100)

print(my_mon.my_money())


class Point:

    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = [Point(2 * i + 1, 2 * i + 1) for i in range(0, 1000)]
points[1].color = 'yellow'

from random import randint


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d
        return self.sp, self.ep


elements = []

p = [randint(1, 3) for i in range(10)]

j = 0
for i in p:
    if i == 1:
        p[j] = ('Line', randint(1, 100), randint(1, 100))
    elif i == 2:
        p[j] = ('Rect', randint(1, 100), randint(1, 100))
    elif i == 3:
        p[j] = ('Ellepse', randint(1, 100), randint(1, 100))
    j += 1


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


elements = [(Line, Rect, Ellipse)[randint(0, 2)](1, 2, 3, 4) for n in range(217)]

a = 1
b = 2
c = 3

elements1 = [(a, b, c)[randint(0, 2)] for n in range(217)]
print(elements1)


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: type(x) in (float, int), (self.a, self.b, self.c))):
            return 1
        if not all(map(lambda x: x > 0, (self.a, self.b, self.c))):
            return 1
        a, b, c = self.a, self.b, self.c
        if a >= b + c or b >= a + c or c >= a + b:
            return 2
        else:
            return 3


tr = TriangleChecker(a, b, c)

print(tr.is_triangle())


class Graph:
    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True

    def set_data(self, data):
        self.data = data[:]

    def my_funckcion(self):
        return ' '.join(map(str, self.data))

    def my_proverka(self):
        if self.is_show == False:
            print('Отображение данных закрыто')
    def show_table(self):
        self.my_proverka()
        print(*self.data)
        print(' '.join(map(str, self.data)))
    def show_graph(self):
        self.my_proverka()
        print(f'Графические отображение данных:{self.my_funckcion()}')

    def show_bar(self):
        self.my_proverka()
        print(f'Столбчатая диаграмма: {self.my_funckcion()}')

    def set_show(self, fl_show):
        self.is_show = fl_show

gr = Graph([8, 11, 10, -32, 0, 7, 18])
gr.set_show(False)
gr.show_table()
gr.show_graph()
gr.show_bar()


class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *mems):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mems[:self.total_mem_slots]
    def get_config(self):
        return [f' материнская плата: {self.name}',
        f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
        f'Слотов памяти: {self.total_mem_slots}',
        'Память: '+ "; ".join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]

mb = MotherBoard('MSI', CPU('AMD', 3455), Memory('Kingston', 2400), Memory('Kingston', 2400))


print(mb.get_config())


class Cart:
    def __init__(self):
        self.goods = []
    def add(self, gd):
        self.goods.append(gd)
    def remove(self, indx):
        self.goods.pop(indx)
    def get_list(self):
        return[f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self. price = price

class TV:
    def __init__(self, name, price):
        self.name = name
        self. price = price

class Notebook:
    def __init__(self, name, price):
        self.name = name
        self. price = price

class Cup:
    def __init__(self, name, price):
        self.name = name
        self. price = price

cart = Cart()

cart.add(TV('Sony', 355))
cart.add(TV('Samsung', 1355))
cart.add(Table('угловой', 3434))
cart.add(Notebook('Acer', 876))
print(cart.get_list())


import sys

lass
ListObject:


def __init__(self, data):
    self.data = data
    self.next_obj = None

def link(self, obj):
    self.next_obj = obj



# считывание списка из входного потока (эту строку не менять)
lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

head_obj = ListObject(lst_in[0])
obj = head_obj

for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new



class
