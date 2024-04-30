class Point:
    color = 'red'
    circle = 2


print(Point.__dict__)

a = Point()
print(a.color)
print(type(a))

b = Point()

Point.circle = 5
print(a.circle)
b.circle
print(b.circle)
a.color = 'green'
print(a.__dict__)
print(b.color)
Point.type_pt = 'disc'

print(a.type_pt)

setattr(Point, 'prop', 4.5)

print(a.prop)

