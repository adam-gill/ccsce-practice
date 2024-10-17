def create_butterfly(inp: int) -> str:
    res = ""
    even = True
    max_num = inp // 2

    if inp % 2 != 0:
        even = False
        max_num += 1

    for i in range(max_num, 0, -1):
        if i == 1:
            res += f"{i}"
        else:
            res += f"{i} "

    if even:
        res += " " + res[::-1]
    else:
        res += res[::-1][1:]
    
    

    return res


        

        


    return res

def butterfly():
    res_list = []
    cases = []

    num_cases = int(input())

    for _ in range(num_cases):
        case = int(input())
        cases.append(case)
    
    for case in cases:
        res_list.append(create_butterfly(case))


    for r in res_list: print(r)