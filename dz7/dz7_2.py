number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

#1
user_list = [i for i in range(number1, number2 + 1)]
print(*user_list)

#2
print(*user_list[::-1])

#3
print(*[i for i in user_list if i % 7 == 0])

#4
print(len([i for i in user_list if i % 5 == 0]))