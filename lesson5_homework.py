def no_paramet ():
    print('Без параметра')

# for ell_ in [1, 2, 3, 4]:
#     no_paramet()
#     print(ell_)

# def elem(a):
#     a2 = a % 2
#     return a2
# for ele in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     if elem(a=ele) == 0:
#         print('CHETNOE ', ele)
#     else:
#         print('NE CHETNOE ', ele)

def puzir (a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                b = a[j+1]
                a[j+1] = a[j]
                a[j] = b
    return a
from random import randint
N = 10
s = []
for i in range(N):
    s.append(randint(1, 20))
print(s)
g = puzir(a=s)
print(g)



