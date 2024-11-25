num1 = int(input("Введите начало диапозона: "))
num2 = int(input("Введите конец диапозона: "))

number = []

for i in range(num1, num2 + 1):
    if num2 % i == 0:
        number.append(i)
        
    else:
        continue

print(number)