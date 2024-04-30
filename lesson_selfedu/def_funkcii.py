def send_mail():
    text = ("Помогите")
    print(text)


send_mail()
b = 4


def get_sqrt(x):
    res = None if x < 0 else x ** 0.5
    return res


a = get_sqrt(49)
print(a)


def get_max2(a, b):
    return a if a > b else b


x, y = 5, 9

print(get_max2(x, y))


def even(x):
    return x % 2 == 0

for i in range(1, 11):
    if even(i):
        print(i)
