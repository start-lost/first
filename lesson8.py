



class Human:
    _name: str
    _location: str

    def __init__ (self, name='Ivan'):
        self._name = name
        self._location = 'Sochi'

    def get_name(self):
        return self._name
    def get_location(self):
        return self._name + ': ' + self._location

    def set_location(self, location):
        self._location = location

class Children(Human):
    __age = 5

    def __init__(self, name='Fedya'):
        super().__init__(name)

    def set_age(self, age=56):
        self.__age = age

    def get_age(self):
        return self._name + ': ' + str(self.__age)


class Bus:
    __child: list()

    def __init__(self, child: list()):
        self.__child = child

    def add_childs(self, child: list()):
        self.__child = self.__child + child

    def del_childs(self, child: list()):
        for i in child:
            if i in  self.__child:
                self.__child.remove(i)
    def info_bus(self):
        for i in self.__child:
            print(i.get_location())

    def go_loc(self, new_loc):
        for i in self.__child:
            i.set_location(new_loc)

# a = Human()
# print(a.get_location())
# ch = Children()
# ch.set_age(77)
# print(ch.get_location())
# print(ch.get_age())

a0 = Children()
a1 = Children('Petya')
a2 = Children('Sveta')
a3 = Children('Katya')
a4 = Children('Masha')


b1 = Bus([a0, a1, a2, a3])
b1.info_bus()
print('-----------------------')
b1.go_loc('Moscow')
b1.info_bus()
print('-----------------------')
b1.add_childs([a4])
b1.info_bus()
print('-----------------------')
b1.del_childs([a0, a1, a2, a3])
b1.info_bus()

list1 = [1, 2, 3, 4, 'hello', 5, 6]

def list88(list00: list):
    list2 = list()
    for i in list00:
        try:
            list2.append(i/(i-2))
        except ZeroDivisionError:
            print('Делить на ноль нельзя!!!')
        except Exception as e:
            print('Текстовое поле')
        finally:
            print(i)
    return list2
print(list88(list1))
