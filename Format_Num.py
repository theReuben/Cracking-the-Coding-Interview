# This program converts an int to a string with comma seperations.
# It takes two command line arguments, the first is the int, and the second is the comma style
# EN style has comma seperations as follows: 1,000,000,000
# IN style has comma seperations as follows: 1,00,00,00,000

import sys

style_guide = {"EN" : [3,3], "IN" : [3,2]}

def format_num(num, style) :
    """
    style = EN, for English style
    style = IN, for Indian style
    """
    num = str(num)
    i = len(num)-style_guide[style][0]
    while (i > 0) :
        num = num[:i] + ',' + num[i:]
        i -= style_guide[style][1]
    return num


if __name__ == "__main__" :
    num = int(sys.argv[1])
    style = sys.argv[2]
    print (format_num(num, style))
