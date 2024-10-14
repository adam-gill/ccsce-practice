#2021 Problem 2

def vowel_mvmt(): 
    vowels = ["a", "e", "i", "o", "u"]
    res_list = []
    mem = []
    

    while True:
        vowel_list = []
        res = ""
        line = input()
        if line == "quit" or line == "EOF": break

        for c in line:
            if c.lower() in vowels:
                vowel_list.append(c.lower())

        vowel_list.sort()
        
        for c in line:
            if c.lower() in vowels:
                if c.isupper():
                    res += vowel_list[0].upper()
                else:
                    res += vowel_list[0]
                vowel_list.pop(0)
            else:
                res += c

        res_list.append(res)
    
    for r in res_list: print(r)

"""
input.txt:

The rain in Spain falls mainly on the plain
A strong smell of turpentine prevails throughout
O Canada! Our home and native land!
quit

"""


