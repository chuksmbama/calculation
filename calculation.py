from secrets import choice


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print('Welcome to simple calculator')
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
print('(1) Addition\n(2) substraction\n(3) Multiplication\n(4) Division')
choice = int(input('Enter the operation you will like to work with: 1, 2, 3, 4: '))

if choice == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif choice == 2:
    print(num1, '-', num2, '=', sub(num1, num2))
elif choice == 3:
    print(num1, 'x', num2, '=', mul(num1, num2))
elif choice == 4:
    print(num1, '/', num2, '=', div(num1, num2))
else:
    print('Sorry, cannot input')

print('Do you want to still carry out any operation (1) yes\n(2) No')
ans = int(input('Enter: 1 or 2: '))

if ans == 1:
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    print('(1) Addition\n(2) substraction\n(3) Multiplication\n(4) Division')
    choice = int(input('Enter the operation you will like to work with: 1, 2, 3, 4: '))

    if choice == 1:
        print(num1, '+', num2, '=', add(num1, num2))
    elif choice == 2:
        print(num1, '-', num2, '=', sub(num1, num2))
    elif choice == 3:
        print(num1, 'x', num2, '=', mul(num1, num2))
    elif choice == 4:
        print(num1, '/', num2, '=', div(num1, num2))
    else:
        print('Sorry, cannot input')
else:
    print('Thank you')

    
