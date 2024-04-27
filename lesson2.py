list1 = [1, 2, 3, 'hello!']

list2 = [5, 5, 6, 6, 7, 7, 'hello!']

list2 = list(set(list2))

print(list2)
print(list1)
print(list1[0])

d1 = dict()
d1["first"] = 1
d1["second"] = 12345

d1["first"] = 222
print(d1)
print(d1.get("first"))
d2 = {
    "val1": 1,
    "val2": 2,
    "val3": 3,
    1: 'test'
}
print(d2.values())
print(d2.keys())
d3=dict()
d3['new'] = d2
d3['old'] = None
#print(d3.get('new').get('val2'))