# my solution - kinda sucks

def roman_numerals():

    res_list = []
    numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    while True:
        # handle input
        line = input()
        if line == "quit" or line == "" or line == "EOF":
            break

        res = 0

        if len(line) == 1:
            res += numerals[line[0]]
            res_list.append(res)
            break

        while len(line) > 0:
            if len(line) == 1:
                res += numerals[line[0]]
                break

            l_val = numerals[line[0]]
            r_val = numerals[line[1]]


            if l_val < r_val:
                res += r_val - l_val
                line = line[2:]

            elif l_val >= r_val:
                res += l_val
                line = line[1:]
            

        res_list.append(res)

    for r in res_list:
        print(r)

def roman_numerals2():
    # ex: MMMDCCXLIX

    res_list = []
    numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    while True:
        # handle input
        line = input()
        if line == "quit" or line == "" or line == "EOF":
            break
        
        res = 0

        for i in range(len(line)):
            val = numerals[line[i]]

            if i == len(line) - 1:
                res += val
            elif val >= numerals[line[i + 1]]:
                res += val
            else:
                res -= val
        
        res_list.append(res)

    for r in res_list:
        print(r)

# int to roman
def roman_numerals3(num: int) -> str:
    
    res = ""

    numerals = {
        "M": 1000,
        "CM": 900, 
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }

    for symb, val in numerals.items():
        while num >= val:
            num -= val
            res += symb
    
    return res

# print(roman_numerals3(3749))