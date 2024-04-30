class DataBase:
    pk = 1
    title = "Классы и объекты"
    autor = "Косов Данил"
    views = 14356
    comments = 12


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024
Goods.price = 2048
setattr(Goods, 'inflation', 100)
setattr(Goods, 'price', 4096)

print(Goods.price)
print(Goods.inflation)

class Car:
    pass


setattr(Car, "model", "Тойота")
setattr(Car, 'color', 'Розовый')
setattr(Car, 'number', "П111УУ77")


print(Car.model)
print(Car.color)
print(Car.number)

class Notes:
    pass

setattr(Notes, 'uid', 1005435)
setattr(Notes, 'title', 'Шутка')
setattr(Notes, 'autor', 'И.С.Бах')
setattr(Notes, 'pages', 2)

print(getattr(Notes, 'autor'))


class Dictionary:
    rus = "Питон"
    eng = "Puthon"

print(getattr(Dictionary, 'rus_word', False))


