#!/usr/bin/python3
import sys

def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    vel = [int(i) for i in str(num)]
    sorted(vel)
    j = ""
    import datetime
    a = datetime.datetime.now()
    for i in sorted(vel):
        j = str(i) + j
        final = -1
        for i in range(int(num)+1,int(j)):
            num = [int(l) for l in str(i)]
            if sorted(num) == sorted(vel):
                final = i
                break
    return final

if __name__ == "__main__":
    main()



