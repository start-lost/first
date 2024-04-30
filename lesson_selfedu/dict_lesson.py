d = {
    "house": "дом",
    "car": "машина",
    "tree": "дерево",
    "road": "дорога",
    "river": "река"
}
print(d["car"])

ff = dict(one=1, two=2, three='3', four='4')

print(d)
d2 = d.copy()
d2["car"] = 'ветка'
print(d2)
print(d)