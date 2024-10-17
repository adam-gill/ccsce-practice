def create_fence(inp) -> str:
    res = ""
    posts = int(inp[0])
    post = inp[1]
    fence = inp[2]

    for p in range(posts):
        print(p, posts)
        res += post
        if p != posts - 1: res += fence

    return res



def fences():

    res_list = []
    cases = []

    num_cases = int(input())

    for _ in range(num_cases):
        case = input()
        cases.append(case.split())
    
    for case in cases:
        res_list.append(create_fence(case))
        

    for r in res_list: print(r)
        