user_input = int(input("Введите число от 1 до 100: "))

if user_input %3 == 0 and user_input %5 == 0:
        print("Fizz Buzz")

elif user_input %3 == 0 or user_input %5 == 0:
    if user_input %3 == 0:
        print("Fizz")
    if user_input %5 == 0:
        print("Buzz")

    else:
        print(user_input)

else:
     print("Введите число в дапозоне от 1 до 100!")