class Human:
    hands = int
    foot = int
    head = int
    eyes = int
    age = int
    sex = 1
    name = str

    def __init__(self, v_name):
        self.hands = 2
        self.foot = 2
        self.head = 1
        self.eyes = 2
        self.age = 30
        self.sex = 1
        self.name = v_name

    def mobilize(self):
        if self.sex == 1:
            self.hands = self.hands / 2
            self.foot = self.foot / 2
            self.eyes = self.eyes / 2

    def see_info(self):
        print(f'name = {str(self.name)}')
        print(f'hands = {str(self.hands)}')
        print(f'foot = {str(self.foot)}')
        print(f'head = {str(self.head)}')
        print(f'eyes = {str(self.eyes)}')
        print(f'age = {str(self.age)}')
        print(f'sex = {str(self.sex)}')

    def __str__(self):
        return self.name

class Woman(Human):
    def __init__ (self, v_name):
        super().__init__(v_name)
        self.sex = 0
        self.cicle = 28

    def see_info(self):
        super().see_info()
        print(f'cicle = {str(self.cicle)}')

# o_petya = Human("Petya")
# o_petya.see_info()
#
# o_vasya = Human("Vasya")
# o_vasya.see_info()
# o_vasya.mobilize()
# o_vasya.see_info()

o_masha = Woman("Masha")
o_masha.see_info()