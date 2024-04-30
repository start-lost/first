d = [1, 2, 3, 4, 5, 6]
s = ''
c = ["Pyton", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
for i in c:
    s +=i+" "
print(s.lstrip())
print(" ".join(c))

digs = [4, 3, 100, -53, -30, 1, 34, -8]

for i, b in enumerate(digs):
    if 10 <= abs(b) <= 99:
        digs[i] = 0

print(digs)

