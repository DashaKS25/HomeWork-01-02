#Перевірити, чи є число не парним, ділиться чи на три і на п'ять одночасно, але так, щоб не ділитися на 10.
a = int(input('Enter number'))
if a % 2 != 0:
    print('Умова виконана')
else:
    print('Умова не виконана')
if (a % 3 == 0) and (a % 5 == 0):
    print('Йдемо далі')
elif a % 10 != 0:
    print('Перевірка закінчена')


