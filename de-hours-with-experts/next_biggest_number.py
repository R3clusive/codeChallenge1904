#!/usr/bin/python3
import sys
from itertools import permutations 
  
def main():
    next_biggest_number(sys.argv[1])


def combine(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s



def next_biggest_number(num):
 n = len(str(num))
 res = [int(x) for x in str(num)] 
 comb = permutations(res, n) 
 ListOfPossibilities = list()
 for i in comb: 
    ListOfPossibilities.append(combine(i))
 ListOfPossibilities = sorted(ListOfPossibilities)
 for i in ListOfPossibilities:
    y = 0
    if(i > num):
            y=1
            return i
 if(y==0):
    return -1



if __name__ == "__main__":
    main()



