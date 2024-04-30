import sys


class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open('filemedia1')
media2.open('filemedia2')

media1.play()
media2.play()


class Graps:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        self.stroka =[]
        for i in self.data:
            if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
                self.stroka.append(i)
        print(*self.stroka)


grapf_1 = Graps()

grapf_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])

grapf_1.draw()


class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr ={}
        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)
    def remove(self, eng):
        self.tr.pop(eng, False)
    def translate(self, eng):
        return self.tr[eng]

tr = Translator()

tr.add('tree','дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river','река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk','молоко')
print(*tr.translate('go'))



