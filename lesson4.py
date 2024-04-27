l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [100, 200, 1]

v_sum = 0
for one_el in l1:
    if one_el % 2 == 0:
        v_sum += one_el
print(v_sum)

# for one in l1:
#     print(one)
#     print(one*10)


d1 = {
    'ONE':123,
    'TWO':456
}


# for one_d1 in d1.keys():
#     print(one_d1, d1.get(one_d1))


# i = 1
# d2 = dict()
#
# for one_element in l1:
#     d2[i] = one_element
#     i = i + 1
# print(d2)
i = 0
j = 0
import time
for one_element in [1, 2, 3]:
    j += 1
    while j < 5:
        print(f'one element = {str(one_element)}')
        print('Hello!', i)
        i += 1
        time.sleep(1)

