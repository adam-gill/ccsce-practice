def create_infinity_word(inp: list[str]) -> str: 
    s = int(inp[0])
    text = inp[1]
    snapped = ""
    left = ""

    for i in range(len(text)):
        if i % s == 0:
            snapped += text[i]
        else:
            left += text[i]

    return left + snapped[::-1]

def infinity_words():
    res_list = []
    cases = []

    num_cases = int(input())

    for _ in range(num_cases):
        case = input()
        cases.append(case.split())
    print("num cases: " + str(len(cases)))
    
    for case in cases:
        res_list.append(create_infinity_word(case))
    
    for r in res_list: print(r)

