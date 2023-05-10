#Перевірити, чи є введене число парним.
a = int(input('Enter number'))
if a % 2 == 0:
    print('Good')
elif not a % 2 == 0:
    print('Try again')
