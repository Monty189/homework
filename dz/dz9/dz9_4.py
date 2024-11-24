translation_table = str.maketrans("", "", "36")

user_input = str(input("Введите чилсо: "))

result = user_input.translate(translation_table)

print(result)