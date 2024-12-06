#user_input = int(input("Введите длинну стороны квадрата: "))
#for i in range(user_input):
#    for j in range(user_input):
#        print(" * ", end=' ')
#    print("\n")

def draw_triangle(fill, base=10): # Буква Б
    n = 1
    for  i in range(base):
        i = [fill] * n
        print (' '.join(i))
        n += 1

draw_triangle(' * ')

print("------------------------------------------------")

def draw_triangle(fill, base=10): # Буква И
    n = 10
    for i in range(base):
        i = [fill] * n
        print (' '.join(i))
        n -= 1

draw_triangle(' * ')

print("------------------------------------------------")

n = 5 # Буква К
for i in range(n):
    for j in range(n):
        if j >= n - 1 - i:  # Условие для закрашивания половины
            print("*", end = " ")
        else: 
            print(" ", end = " ")
    print() # Переход на новою строку после каждой строки

print("------------------------------------------------")

n = 5 # Буква К
for i in range(n):
    for j in range(n):
        if j <= n - 1 - i:  # Условие для закрашивания половины
            print("*", end = " ")
        else: 
            print(" ", end = " ")
    print() # Переход на новою строку после каждой строки