user_input = int(input("Сколько секунд прошло: "))
hour = round(user_input / 3600, 2) # Секунд в часе 
min = round(user_input / 360, 2)  # Минут в часе
sec = user_input // 60 # Целых секунд в минуте
print(f"{hour}\n{min}\n{sec}")