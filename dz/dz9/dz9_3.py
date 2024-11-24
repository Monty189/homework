count = 0



for number in range (100,10000):
    digits = str(number)
    

    if len(str(digits)) == 3:
        if (digits[0] != digits[1] and digits[0] != digits[2] and digits[1] != digits[2]):
            print(digits)
            count += 1
            
        

    elif len(str(digits)) == 4:
        if (digits[0] != digits[1] and digits[0] != digits[2
        ] and digits[0] != digits[3] and digits[1] != digits[2
        ] and digits[1] != digits[3] and digits[2] != digits[3]):
            print(digits)
            count +=1
            
            
print(count)