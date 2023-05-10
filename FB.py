a = int(input('Введіть fizz: '))
b = int(input('Введіть buzz: '))
c = int(input('Додайте число до якого треба порахувати: '))
numbers = []
with open('numbers.txt', 'r') as f:
    [print(i % a//b*'F'+i % a//b*'B' or i+1) for i in range(1, c + 1)]