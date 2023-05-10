age = int(input('How old are you'))
if age >= 100:
    print('person is lying')
elif age >= 18:
    print('all is good')
else:
    print('not good')
if age % 2 == 0:
    print('even')
else:
    print('not even')
name = input('Enter your name please')
if 'a' in name:
    print('We dont check you')
elif ('v' in name or 'V' in name) and age % 2 == 0:
    print('YOU WIN PRIZE')
else:
    print('Sorry you dont win')



