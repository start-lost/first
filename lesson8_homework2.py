class Soda:
    def __init__(self, dobavka=None):
        if isinstance(dobavka, str):
            self.dobavka = dobavka
        else:
            self.dobavka = None
    def show_my_drink(self):
        if self.dobavka != None :
            print(f'Газировка и {str(self.dobavka)}')
        else:
            print('Обычная газировка')
            print(self.dobavka)

g1 = Soda(56)
g2 = Soda('Cola')
g1.show_my_drink()
g2.show_my_drink()


class KgtoPoud:
    kg_new = str
    kg_old = str
    def __init__(self, kg):
        self.__kg=kg
    def to_poud(self):
       if type(self.kg_new) == int:
           self.kg_old = self.__kg
           self.__kg = self.kg_new
       return self.__kg*2.205

    def set_kg(self, kg_new):
        self.kg_new = kg_new

    def get_kg(self):
        if type(self.kg_old) == int:
            return self.kg_old
        else:
            return self.__kg



kg = KgtoPoud(12)
print(f'Масса в Фунтах = {str(kg.to_poud())}')
kg.set_kg(41)
print(f'Масса в Фунтах = {str(kg.to_poud())}')
print(f'Старая масса = {str(kg.get_kg())}')

class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.age = age
        if name == 'Николай':
            self.name = name

        else:
            self.name = f'Я не {name}, а Николай'

a1 = Nikola('Николай', 43)
a2 = Nikola('Вася', 56)
print(a2.name)
a2.surname = 'Николай'
print(a2.surname)
