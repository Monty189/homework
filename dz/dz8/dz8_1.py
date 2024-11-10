num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

user_list = [i for i in range(num1, num2 + 1)]
print(*user_list)

odd = [i for i in user_list if i % 2 !=0] # Нечетные
print(*odd)
even = [i for i in user_list if i % 2 == 0 and i !=0] # Четные
print(*even)
for_nine = [i for i in user_list if i % 9 == 0] # Кратные девяти
print(*for_nine)

print("Среднее арифметическое нечетных: ", sum(odd) / len(odd))
print("Среднее арифметическое четных: ", sum(even) / len(even))
print("Среднее арифметическое кратных девяти: ", sum(for_nine) / len(for_nine))