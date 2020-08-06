#!/usr/bin/python3
'''
It demostrates how to interpret a nested list comprehension
'''

a = "30 PLN,12 USD,9 EUR,307 GBP"
q = [x for pair in a.split(',') for i, x in enumerate(pair.split(' ')) if i == 0]
print(q)
