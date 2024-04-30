class Point:
    color = 'red'
    circle = 2

    def set_coords(self):
        print("вызов метода set_coords " + str(self))

pt = Point()
pt.set_coords()
