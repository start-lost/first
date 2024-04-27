class Bus:
    mest = list
    dety = list
    mesta = list
    name = str
    name_uhod = 0
    mesto = int

    def __init__(self, school):
        self.dety = ['katya', 'sasha', 'masha', 'petya']
        self.mesta = list()
        j = 1
        for i in self.dety:
            self.mesta.append(j)
            j += 1
        self.name = school

    def out_bus(self, vihod, mesto):
        if vihod == 1:
            self.name_uhod = self.dety[mesto-1]
            self.dety[mesto-1] = 0




    def vivod(self):
        print(f'dety = {str(self.dety)}')
        print(f'mesta = {str(self.mesta)}')
        print(f'school = {str(self.name)}')
        if self.name_uhod !=0:
            print(f'yshol = {str(self.name_uhod)}')




a = Bus("pervaya")
a.vivod()
a.out_bus(1, 2)
a.vivod()
a.out_bus(1, 1)
a.vivod()
a.out_bus(1, 3)
a.vivod()