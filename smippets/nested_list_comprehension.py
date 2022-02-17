#!/usr/bin/python3
'''
It demostrates how to interpret a nested list comprehension
'''

rate = {"PLN": 1, "USD": 3.73, "EUR": 4.42, "GBP": 4.88}
bill = "30 PLN,12 USD,9 EUR,306 GBP"
tokens = [col for line in bill.split(' ') for col in line.split(',')]
#tokens = [col for line in bill.split(',') for col in line.split(' ')] works too
total = [float(item[0]) * rate[item[1]] for item in zip(tokens[::2], tokens[1::2])]
print('{}, sum = {}'.format(total, sum(total)))

'''
Outputs: [30.0, 44.76, 39.78, 1493.28], sum = 1607.82
'''
