from timeit import Timer


# append
def test1():
    lis = []
    for i in range(1000):
        lis.append(i)


# +
def test2():
    lis = []
    for i in range(1000):
        lis += [i]


# []
def test3():
    lis = [i for i in range(1000)]
    return 0

# list()


def test4():
    lis = list(range(1000))
    return 0


# timeit Timer
t1 = Timer('test1()', 'from __main__ import test1')
print(f'append \n {t1.timeit(number = 10000)}')
t2 = Timer('test2()', 'from __main__ import test2')
print(f'add,+ \n {t2.timeit(number = 10000)}')
t3 = Timer('test3()', 'from __main__ import test3')
print(f'[] \n {t3.timeit(number = 10000)}')
t4 = Timer('test4()', 'from __main__ import test4')
print(f'list() \n {t4.timeit(number = 10000)}')
