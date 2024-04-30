age = 18
name = "Sergei"

print('Menia zovut {fio}, mne {old} let'.format(fio=name, old=age))

"""PEP498 https://www.python.org/dev/peps/pep-0498/"""

print(f'Menia zovut {name}, mne {age*2} let')

print(f'Menia zovut {name.upper()}, mne {age*2} let')

print(f'Menia zovut {len(name)}, mne {age*2} let')

print(len('123456'))

d=list('0123456789')
print(sorted(d, reverse= True))

j = 0
for i in d:
    d[j] = int(i)
    j += 1

print(d)
d = sorted(d, reverse=True)
print(d)

b=list('gram')
c=d+b
print(c)
print(50 in d)
print(d[3:9])