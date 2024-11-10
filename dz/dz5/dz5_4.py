number=list(map(float, (input("Введите два числа через пробел: ")).split()))

if number[0] == number[1] :
    pass
else:
    print(sorted(number))