
# Online Python - IDE, Editor, Compiler, Interpreter


def sum(a, b):
    return (a + b)
def mul(a, b):
    return (a * b)
def sub(a, b):
    return (a - b)
def div(a, b):
    return (a / b)

c = int(input('Choose action (1/2/3/4): Sum, Multiply, Substract, Divide'))
a = int(input('Enter 1st number: '))

if c == 4:
    b = int(input('Enter 2nd number: '))
    while b == 0:
        b = int(input('2nd number cant be zero, choose new number: '))
else:
    b = int(input('Enter 2nd number: '))



if c == 1:
    print(f'Sum of {a} and {b} is {sum(a, b)}')
elif c == 2:
    print(f'Multiplied {a} and {b} is {mul(a, b)}')
elif c == 3:
    print(f'Substraction of {a} and {b} is {sub(a, b)}')
elif c == 4:
    print(f'Dividing {a} and {b} is {div(a, b)}')
else:
    print('Wrong number. Choose between 1-4!')


