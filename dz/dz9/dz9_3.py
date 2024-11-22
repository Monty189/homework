count = 0

for number in range (100,10000):
    digits = str(number)

    if (digits[0] != digits[1] != digits[2]) or 
        count += 1
        print(digits)

print(count)