test_list = [1, 2, 3, 4]
# <editor-fold desc="simple print">
print('\nsimple print\n')
print('test_list', test_list)
print('*test_list', *test_list)
# </editor-fold>

# <editor-fold desc="test_func">
print('\ntest_func\n')


def test_func(some_list):
    print(*some_list)


test_func(test_list)
# </editor-fold>

# <editor-fold desc="variadic functions">
print('\nvariadic functions\n')


def sum_it(*args):
    result = 0
    for num in args:
        result += num
    print(result)


sum_it(test_list)
sum_it(1, 1)
sum_it(1, 2, 3, 4, 5)

"""
def sum_it(*test_list):
    result = 0

    result += test_list
    print(result)


sum_it()"""
# </editor-fold>