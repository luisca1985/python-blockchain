name =  input('Give me your name: ')
age = int(input('Give me your age: '))


def print_function(*args):
    print(*args)


def decades(num: int) -> int:
    return num // 10


print_function(name, age)

print('Decades:', decades(age))