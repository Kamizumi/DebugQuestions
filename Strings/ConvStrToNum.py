def convStrNum(string):
   
    base = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "ten": 10,
            "eleven": 11,
            "twelve" : 12,
            "thirteen" : 13,
            "fourteen" : 14,
            "fifteen" : 15,
            "sixteen" : 16,
            "seventeen" : 17,
            "eighteen" : 18,
            "nineteen" : 19,
            "twenty" : 20,
            "thirty" : 30,
            "forty": 40,
            "fifty": 50,
            "sixty": 60,
            "seventy": 70,
            "eighty" : 80,
            "ninety" : 90,
            "hundred": 100,
    }
    mults = {
            "thousand": 1000,
            "million": 1000000,
            "billion": 1000000000,
            "trillion": 1000000000000}

    string = string.split()
    updatedStr = 0
    grandTotal = 0
    
    for i in range(len(string)):
        if string[i] in base:
            if string[i] == 'hundred':
                updatedStr *= 100
            else:
                updatedStr += base[string[i]]
        elif string[i] in mults:
                if updatedStr == 0:
                    if i == 0:
                        updatedStr += mults.get(string[i])
                    else:
                        grandTotal *= mults.get(string[i])
                else:
                    updatedStr *= mults[string[i]]
                    grandTotal += updatedStr
                    updatedStr = 0
        else:
            pass
    grandTotal += updatedStr
    return f"{grandTotal:,}"
    
    
#print(convStrNum("fifty five million"))
#print(convStrNum("six hundred seventy million"))
print(convStrNum("Nine Hundred Nine"))
print(convStrNum("twelve thousand nine hundred seventy four"))
print(convStrNum("five hundred sixty nine million three hundred twenty four thousand one hundred and twenty three"))
print(convStrNum("nine hundred ninety nine billion nine hundred ninety nine million nine hundred ninety nine thousand nine hundred ninety nine"))
print(convStrNum("five hundred thousand million"))
print(convStrNum("one thousand"))

#Sixty Million
    
    
    