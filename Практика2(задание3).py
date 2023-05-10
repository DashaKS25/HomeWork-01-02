#Ввести число, вивести усі його дільники.
a = int(input('Введіть число'))
b = a
for i in range(1, b + 1):
    if(a % i ==0):
        print(i)


