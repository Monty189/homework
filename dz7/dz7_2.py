number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

#1 Все числа диапозона
user_list = [i for i in range(number1, number2 + 1)]
print(*user_list)

#2 От максимального к минимальному
print(*user_list[::-1])

#3 Кратно семи
print(*[i for i in user_list if i % 7 == 0])

#4 Кол-во кратных пяти
print(len([i for i in user_list if i % 5 == 0]))