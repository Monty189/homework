def user(num):
    if user_input == 1:
        return "Максимум: ", max(numbers)
    elif user_input == 2:
        return "Минимум: ", min(numbers)
    elif user_input == 3:
        return "Среднее арифметическое: ", sum(numbers)/3
    else:
        return "Ошибка!"
    
numbers = []
numbers = list(map(float, (input("Введите три числа через пробел: ").split())))
user_input = int(input("Выберите действие\n1.Максимум\n2.Минимум\n3.Среднее арифметическое:\n"))

print(*user(user_input))