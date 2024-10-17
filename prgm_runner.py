import sys

from prblms2021.butterfly import butterfly

with open('input.txt', 'r') as f:
    sys.stdin = f
    print("******************** Program Start ********************")
    butterfly()
    print("******************** Program End **********************")