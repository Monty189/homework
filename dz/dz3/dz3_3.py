user_input = float(input("Введите количество метров: "))
answer = input("Превести в\n1.Сантиметры\n2.Дицемтры\n3.Миллиметры\n4.Мили\nВыберите число от 1 до 4: ")

if answer == "1":
    print(f"{round(user_input * 100 , 6)}{" см."}")

elif answer == "2":
    print(f"{round(user_input * 10 , 6)}{" дм."}")

elif answer == "3":
    print(f"{round(user_input * 1000, 6)}{" мм."}")

else :
    print(f"{round(user_input * 0.00062137 , 6)}{" мили."}")