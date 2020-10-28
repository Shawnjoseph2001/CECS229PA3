def myFilter(L, num):
    for i in L:
        if not (i % num == 0):
            L.remove(i)
    return L


def my_lists(L):
    ret = []
    for i in L:
        ret2 = []
        for j in range(i):
            ret2.append(j)
        ret.append(ret2)
    return ret


def my_function_composition(f, g):
    ret = {}
    for i in f:
        ret.append(i, g.get(i))
    return ret


def mySum(L):
    current = 0
    for x in L:
        current = current + x
    return current


def myProduct(L):
    current = 1
    for x in L:
        current = current * x
    return current


def myMin(L):
    current = L[0]
    for x in L:
        current = min(current, x)
    return current
