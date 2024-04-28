class Human:
    name: str
    age: str
    location: str

    def __init__(self, na='Oleg'):
        self.name = na

    def set_loc(self, loc='Volgograd'):
        self.location = loc

    def get_info(self):
        return self.name + ' ' + self.location

class Rota:
    ima: list()

    def __init__(self, im: str):
        self.ima = im
    def add_men(self, name1: list()):
        self.ima = self.ima +name1
    def info_rota(self):
        for i in self.ima:
            print(i.get_info())

class Polk:

    def __init__(self, polk='First'):
        self.polk=polk
    def add_rota(self, rota: str):
        self.polk =self.polk + rota
    def info_polk(self):
        for i in self.polk:
            print(i.info_rota())


a0 = Human('Kolya')
a0.set_loc('Volgograd')
a1 = Human('Vasia')
a1.set_loc('Kaliningrad')
a2 = Human('Nikita')
a2.set_loc('Yakutsk')
a3 = Human('Masha')
a3.set_loc('Sochi')



r1 = Rota("Pervaiy")

p1 = Polk("ROMA")
p1.add_rota(r1)

