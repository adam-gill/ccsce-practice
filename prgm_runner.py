import sys

from prblms2022.registers import registers

with open('input.txt', 'r') as f:
    sys.stdin = f
    print("******************** Program Start ********************")
    registers()
    print("******************** Program End **********************")