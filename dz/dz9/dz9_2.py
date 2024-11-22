num = list(map(str, range(100, 1000)))

all = []

for i in num:
    for n in i:
        if i.count(n) > 1:
            all.append(i) if i not in all else None

print(len(all)) 