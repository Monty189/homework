print('Выбрать тему для написания романа')
print('Найти всю необходимую информацию для написания романа')
print('Создать структуру будущей книги')
print('Начать писать книгу')


while True:
    answer=input('Информации хватает для написания главы?\n(да,нет): ')
    if answer == 'нет':
        print('Найти недостающую информацию')
    else:
        break

print('Продолжить писать книгу')
print('Проверить написанное')

while True:
    answer2=input('Все верно?\n(да,нет): ')
    if answer2 == 'нет':
        print('Продолжить редактирование')
    else:
        break

print('Отправить книгу в издательство')