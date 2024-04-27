#l1 = ['one', 'two', 'tree', 'four', 'five', 'Hello']
l01 = ['a', 'b', 'c', 'd', 'i']
l02 = [10, 20, 30, 40, 50]
l03 = [1.1, 2.2, 3.3, 4.4, 5.5]
l0 = [l01, l02, l03]
i = 0
# for element_lista in l0:
#     for ellist in element_lista:
#         print(ellist)
d01 = {
    "one": 1,
    "two": 2,
    "tree": 3,
    "four": 4,
    "five": 5,
    "a": 100,
    "b": 200,
    "f": 1000
}
# for slovar in d01.values():
#     print(slovar)
#
# for kluch in d01.keys():
#     print(kluch)
#print(l1)
# i = 0
# l001 = list()
# print(l001)
# while i != 10000:
#     l001.append(i)
#     i += 1
# print(l001)
l01 = ['a', 'b', 'c', 'd', 'e']
l02 = [10, 20, 30, 40, 50]
l03 = [1.1, 2.2, 3.3, 4.4, 5.5]
d2 = {}
i = 0
while i < len(l01):
    key1 = l01[i]
    value1 = l02[i]
    d2.update({key1: value1})
    i+=1
for key2 in d2.keys():
    d01[key2]=d2.get(key2)

print(d01)


