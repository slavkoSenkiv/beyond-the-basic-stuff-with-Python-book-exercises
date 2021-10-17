# semicolon usage
x = 'hey'; x = x * 2; print(x)

# if, while, for, def, or class statements, a single-line block
x = 11; y = 10
if x < y: print(f'{x} < {y}')
else: print(f'{x} !< {y}')
while x > 5: print(x); x -= 1
for i in range(y): print('a' * i)

def x(): print('smth')

x()