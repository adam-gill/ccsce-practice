def eval_case(case) -> str:
    res = ""
    reg_dict = {}

    for line in case:
        operation = line[0]
        reg = line[1]
        v1 = line[2].replace("$", "")
        v2 = line[3].replace("$", "")

        if "r" in v1 and v1 not in reg_dict:
            res = "No known constants"
            break
        elif "r" in v1:
            v1 = reg_dict[v1]
        else:
            v1 = int(v1)

        if "r" in v2 and v2 not in reg_dict:
            res = "No known constants"
            break
        elif "r" in v2:
            v2 = reg_dict[v2]
        else:
            v2 = int(v2)

        if operation == "add":
            reg_dict[reg] = v1 + v2
        elif operation == "sub":
            reg_dict[reg] = v1 - v2
        elif operation == "div":
            reg_dict[reg] = v1 // v2
        elif operation == "mul":
            reg_dict[reg] = v1 * v2

    if res != "No known constants":
        for rg, v in reg_dict.items():
            res += f"{rg}={v} "


    return res


def registers():
    res_list = []
    cases = []

    while True:
        num_lines = int(input())

        if num_lines != -1:
            case = []
            for _ in range(num_lines):
                line = str(input())
                case.append(line.replace(",", "").split())
            cases.append(case)
        else:
            break
        
    for c in cases:
        res_list.append(eval_case(c))

    for r in res_list: print(r)