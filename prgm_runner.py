import sys

from prblms2021.fences import fences

with open('input.txt', 'r') as f:
    sys.stdin = f
    print("******************** Program Start ********************")
    fences()
    print("******************** Program End **********************")