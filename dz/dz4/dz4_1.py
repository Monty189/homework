import math

def sum_or_prod(sign):
    if sign == "+":
        return "Результат суммы: ", sum(numbers)
    elif sign == "*":
        return "Результат произведения: ", math.prod(numbers)
    else:
        return "Ошибка!"
    
sign = (input("Выберите действие '+' или '*': "))
numbers = []
numbers = list(map(float, (input("Введите три числа через пробел:").split())))

print(*sum_or_prod(sign))