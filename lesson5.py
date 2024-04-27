def func1():
    print('a')
    print('b')
# for one_element in[1, 2, 3]:
#     func1()

def func2(element):
    print(element, element * 2)

for one in [1, 2, 3]:
    func2(element=one)

def func3(name, surname='Сидоров'):
    print(f'name is {str(name)}, surname is {str(surname)}')

func3(name='Иван', surname='Петров')
func3(name='Иван')

def sum2(a, b):
    s = a + b
    return s
print(sum2(a=1, b=6))

def sum3(c):
    return sum2(c, c)

print(sum3(100))
def any_fun(a, b):
    ss= a + b
    ss2 = a - b
    return ss, ss2
v1, v2 = any_fun(10, 8)
print(v1, a, b)
print(v2)

def fun123 (a: int):
    if type(a) == int:
        return a*2


def fun123(a: str):
    return a

print((fun123(2)))

