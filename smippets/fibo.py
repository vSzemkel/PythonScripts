#!/usr/bin/python3
'''
Takes two integer parameters. First is Fibonacci number to print
and the second is how many subsequent numbers will be printed out
It demonstrates how to use collection.deque as a circular buffer
'''
from collections import deque

# read parameters
first = int(input('First Fibonacci ordered number to print: '))
count = int(input('How many subsequent Fibonacci numbers to print: '))

# initialize buffer
res = []
buf = deque(maxlen=count)
buf.append(1)
buf.append(1)
first -= 2

for i in range(first + count):
    pos = len(buf) - 1
    buf.append(buf[pos] + buf[pos-1])

first += 2
for i,fib in enumerate(buf):
    print("{} ({} digits): {}".format(first + i, len(str(fib)), fib))

