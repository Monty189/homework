user_input = int(input("Введите целое число: "))
user_answer = int(input("Введите степень от 0 до 7: "))
number = [user_input**0, user_input**1, user_input**2, user_input**3, user_input**4, user_input**5, user_input**6, user_input**7]

if user_answer == 0:
    print(number[0])

elif user_answer == 1:
    print(number[1])

elif user_answer == 2:
    print(number[2])

elif user_answer == 3:
    print(number[3])

elif user_answer == 4:
    print(number[4])

elif user_answer == 5:
    print(number[5])

elif user_answer == 6:
    print(number[6])

elif user_answer == 7:
    print(number[7])

else:
    print("Ошибка!")