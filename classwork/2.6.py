n = int(input("Сколько секунд прошло: "))
hour = round(n / 3600, 2) # Секунд в часе
min = (n - hour * 3600) // 60  # Минут в часе
sec = (n - ((hour * 3600) + (min * 60)))  # Целых секунд в минуте
print(f"{hour}\n{min}\n{sec}")