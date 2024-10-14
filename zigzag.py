# 2021 Problem 1

def calc_line(ls: list[int]) -> str:
    if 0 in ls:
        return "Zero Value"
    
    for curr, nxt in zip(ls, ls[1:]):
        if (curr < 0 and nxt < 0) or (curr > 0 and nxt > 0):
            return "No"
    
    return "Yes"

def zigzag() -> list[str]:
    res_list = []

    while True:
        # handle input
        res = ""
        line = input()
        if line == "quit" or line == "" or line == "EOF": break

        # separate into a list of ints
        joined_list = [int(num) for num in line.split()]

        # run zigzag calculation and append to res_list
        res = calc_line(joined_list)
        res_list.append(res)

    for r in res_list: 
        print(r)

"""
input.txt:

1 -2 3 -4
1 -2 3 4 -5
1 -2 0 -3
-4 5 -6
quit
EOF

"""
