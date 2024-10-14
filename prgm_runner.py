import sys

from prblms2021.vowel_mvmt import vowel_mvmt

with open('input.txt', 'r') as f:
    sys.stdin = f
    print("******************** Program Start ********************")
    vowel_mvmt()
    print("******************** Program End **********************")