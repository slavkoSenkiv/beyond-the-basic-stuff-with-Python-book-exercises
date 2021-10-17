print('print_step_name\n')


def test_def_atr(name, greeting='hello'):
    print(greeting, name)


test_def_atr('Bill')
test_def_atr('Jill', 'aloha')
test_def_atr('Timm')
test_def_atr('Jill', 'hey')

print('\nprint_step_name\n')


def print_step_name(step_name_description, indent_size=0):
    print(indent_size * '   ' + step_name_description)


print_step_name('step 1')
print_step_name('step 1.1', 1)
print_step_name('step 1.2', 2)
print_step_name('step 2')
print_step_name('step 3')
print_step_name('step 3.1', 1)
print_step_name('step 3.2', 2)


print('\ntwo_def_attr\n')


def two_def_attr(step_name_description, indent_size=0, stars=0):
    print(indent_size * '   ' + stars * '*' + step_name_description)


num = 1
two_def_attr(f'step{num}');                             num += 1
two_def_attr(f'step{num}', 1);                          num += 1
two_def_attr(f'step{num}', 0);                          num += 1
two_def_attr(f'step{num}', 0, 1);                             num += 1
two_def_attr(f'step{num}', 1, 0);                             num += 1
two_def_attr(f'step{num}', 1, 1);                       num += 1
two_def_attr(f'step{num}', 2, 2);                       num += 1