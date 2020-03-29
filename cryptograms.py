#!/usr/local/Cellar/python@3.8/3.8.1/bin/python3
# chmod 700 cryptograms.py
# cat cryptograms.dat | ./cryptograms.py
# Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
# Case #2: SUBDERMATOGLYPHICFJKNQVWXZ
# Source: https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

from math import gcd
from sys import stdin
from string import ascii_uppercase

def get_int_list():
    return [int(x) for x in stdin.readline().split()]

def read_input():
    ret = []
    cases_count = int(stdin.readline())
    for _ in range(cases_count):
        list1 = get_int_list()
        list2 = get_int_list()
        if list1[1] != len(list2):
            raise SyntaxError("Count of primes doesn't match")
        ret.append((list1[0], list2))
        
    return ret

def resolve(lst):
    gcdarr = []
    for i in range(len(lst) - 1):
        gcdarr.append(gcd(lst[i], lst[i+1]))
    
    # to do hard staff - hendle 'ABABABC' prefix case
    gcdarr.insert(0, lst[0] // gcdarr[0])
    gcdarr.append(lst[-1] // gcdarr[-1])
    srtarr = sorted(list(set(gcdarr)))

    map = {}
    for pos, c in list(enumerate(srtarr)):
        map[c] = pos
    #print(map)

    ret = [ascii_uppercase[map[c]] for c in gcdarr]
    return ''.join(ret)

if __name__ == "__main__":
    job = read_input()
    for i, j in list(enumerate(job)):
        #print("N={}, {}".format(j[0], j[1]))
        case_result = resolve(j[1])
        print("Case #{}: {}".format(i + 1, case_result))


