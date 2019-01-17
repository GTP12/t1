name = "alex"


def f1():
    print(name)


def f2():
    name = "eric"
    return f1


ret = f2()
ret()
