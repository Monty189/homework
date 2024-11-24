num1 = int(input("Введите первое число диапозона: "))
num2 = int(input("Введите второе число диапозона: "))


for one_multiplier in range(num1, num2 + 1):
    for two_multiplier in range(1, 11):
        print(f"{one_multiplier}{"x"}{two_multiplier}{"="}{one_multiplier*two_multiplier}", end='\t')
    print()