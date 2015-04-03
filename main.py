import apfunc

f = open('asd.txt', 'r')
tr = f.read()
tr = tr.split('\n')
for i in range(0, len(tr)):
    tr[i] = tr[i].split()
print tr

ms = int(input('Enter min_support: '))

c = [[], []]
ccount = [[], []]
for i in tr:
    for j in i:
        if j not in c[1]:
            c[1].append(j)
c[1].sort()

for i in c[1]:
    temp = 0
    for j in tr:
        if set(i).issubset(set(j)):
            temp += 1
    ccount[1].append(temp)

l = [[], []]
lcount = [[], []]
for i in range(0, len(c[1])):
    if ccount[1][i] > ms:
        l[1].append(c[1][i])
        lcount[1].append(ccount[1][i])

# --------------------------------------------------- WHILE BEGINS -----------------------------------------------------
k = 2
while len(l[k-1]) > 1:
    c.append(apfunc.gencan(l[k-1]))
    if k > 2:
        c[k] = apfunc.prune(c[k], l[k-1])
    ccount.append([])
    l.append([])
    lcount.append([])

    for i in range(0, len(c[k])):
        ccount[k].append(0)
        for j in tr:
            if set(c[k][i]).issubset(set(j)):
                ccount[k][i] += 1
        if ccount[k][i] > ms:
            l[k].append(c[k][i])
            lcount[k].append(ccount[k][i])

    k += 1
# -------------------------------------------- WHILE ENDS ------------------------------------------------

print c
print ccount
print l
print lcount
