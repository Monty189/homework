while True:
    answer=input('В раковине есть посуда?\n(да,нет): ')
    if answer == 'да':
        print('Возьмите тарелку')
        print('Помойте ее')
    else:
        print('Поздравляю, вы помыли посуду!')
        break

print('Медленно обернитесь на плиту')

answer2=input('Там есть сковородка?\n(да,нет): ')

if answer2 == 'да':
    print('Похоже, сегодня не ваш день')
    print('Возьмите сковородку')
    print('Помойте ее')
    print('Поздравляю, теперь вы точно помыли посуду!')
else:
    print('Поздравляю, вы помыли посуду с первого раза!')