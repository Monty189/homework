def metr(num):
    if user_input == 1:
        return "Мили: ", round((number * 0.000621371), 6)
    elif user_input == 2:
        return "Дюймы: ", round((number * 0.0254), 4)
    elif user_input == 3:
        return "Ярды: ", round((number * 0.9144), 4)
    else:
        return "Ошибка!"

number = float(input("Введите количество метров: "))
user_input = int(input("Выберите велечину перевода\n1.Мили\n2.Дюймы\n3.Ярды:\n"))

print(*metr(user_input))