test_list = [1, 2, 3, 4]
print('test_list', test_list)
print('*test_list', *test_list)


def test_func(some_list):
    print(*some_list)


test_func(test_list)
# _________________________________
print('\nnew stuff\n')
# variadic functions


def sum_it(*args):
    result = 0
    for num in args:
        result += num
    print(result)


sum_it(1, 1)
sum_it(1, 2, 3, 4, 5)


def sum_it(*test_list):
    result = 0

    result += test_list
    print(result)

"""print('\nnew stuff \n')


def append_func(col_values_list):
    modified_values_list = []
    for value in col_values_list:
        if value % 2 == 0:
            modified_values_list.append(value)
    print(modified_values_list)
    return modified_values_list


append_func(test_list)"""

sum_it()