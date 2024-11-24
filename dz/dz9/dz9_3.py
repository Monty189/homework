count = 0

for number in range (100,10000):
    digits = str (number)

    if len(str(digits)) == 3:
        if (digits[0] != digits[1] != digits[2]):

            count += 1
            
        print(digits)

    elif len(str(digits)) == 4:
        if (digits[0] != digits[1] != digits[2] != digits[3]):

            count +=1
        
        print(digits)

print(count)