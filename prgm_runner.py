import sys

from prblms2021.roman_numerals import roman_numerals2

with open('input.txt', 'r') as f:
    sys.stdin = f
    print("******************** Program Start ********************")
    roman_numerals2()
    print("******************** Program End **********************")