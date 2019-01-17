def f1():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in f1()])


def f2():
    return [lambda x, i=i: i * x for i in range(4)]


print([m(2) for m in f2()])
