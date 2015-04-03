def gencan(l):
    c = []
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            tmp1 = l[i]
            tmp2 = l[j]
            t1 = tmp1[-1]
            t2 = tmp2[-1]
            tmp1 = tmp1[:-1]
            tmp2 = tmp2[:-1]
            if (tmp1 == tmp2) & (t1 < t2):
                nqmt = []
                for v in tmp1:
                    nqmt.append(v)
                nqmt.append(t1)
                nqmt.append(t2)
                c.append(nqmt)
    return c


def prune(c, l):
    ct = []
    for x in c:
        tmp = []
        for i in range(0, len(x)):
            tmp.append([])
        for i in range(0, len(x)):
            for j in range(0, len(x)):
                if i != j:
                    tmp[i].append(x[j])
        tmp = sorted(tmp)
        flag = True
        for i in tmp:
            if i not in l:
                flag = False
        if flag:
            ct.append(x)
    return ct
