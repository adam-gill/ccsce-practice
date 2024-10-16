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

    res_list = []
    numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    while True:
        # handle input
        line = input()
        if line == "quit" or line == "" or line == "EOF":
            break
        
        res = 0

        for i in range(len(line)):
            if i == len(line) - 1:
                res += numerals[line[i]]
            elif numerals[line[i]] < numerals[line[i + 1]]:
                res -= numerals[line[i]]
            else:
                res += numerals[line[i]]

        res_list.append(res)

    for r in res_list:
        print(r)