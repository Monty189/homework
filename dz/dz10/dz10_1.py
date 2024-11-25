num1 = int(input("Введите начало диапозона: "))
num2 = int(input("Введите конец диапозона: "))

number = []

for i in range(num1, num2+1):
    count = 0
    for n in range(1, i+1):
        if i % n == 0:
            count += 1
    if count < 3:
        number.append(i) if i != 1 else None
            
        

print(*number)