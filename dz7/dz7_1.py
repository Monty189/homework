number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))

for i in range(number1, number2 + 1):
    if i % 7 == 0:
        print(i, end=" ")