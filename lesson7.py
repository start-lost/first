
#public
#protected
#private


class Human:
    name = str
    __age = int
    def __init__(self, v_name="Vasya"):
        self.name = v_name
        self.__age = 30
        self._pass = "12345"

    def get_age(self): #геттер
        return self.__age

    def set_age(self, v_age: int): #сеттер
        if type(v_age) is int:
            self.__age = v_age

o_vasya = Human()
print(o_vasya.name)
print(o_vasya._pass)

o_vasya.set_age(15.9)
print(o_vasya.get_age())
