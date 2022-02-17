#!/usr/bin/python2

plaintext = "Na chuja mi ta chata z kraja RUS"

def cipher(plainbytes):
    plainbytes = plainbytes[::-1]
    ciphertext = bytearray(32)
    for i in range (0, 8):
        ciphertext[i] = plainbytes[i]
    for i in range (8, 16):
        ciphertext[i] = plainbytes[23-i]
    for i in range (16, 32, 2):
        ciphertext[i] = plainbytes[46-i]
    for i in range (31, 15, -2):
        ciphertext[i] = plainbytes[i]
    return ciphertext

def printbytes(barr):
    print str(barr)
    print str(barr).encode('hex')
    print tuple(barr)

print "*"*100
plainbytes = bytearray(plaintext)
printbytes(plainbytes)
cip = cipher(plainbytes)
printbytes(cip)

# hardcore reversing
hardplain = bytearray(32)
for i,c in enumerate(cip[17:33:2]):
    hardplain[17 + 2*i] = c
for i,c in enumerate(cip[30:14:-2]):
    hardplain[16 + 2*i] = c
hardplain[8:16] = cip[15:7:-1]
hardplain[:8] = cip[:8]
hardplain = hardplain[::-1]
printbytes(hardplain)

# index table
pattern = bytearray([x for x in range(32)])
cippat = cipher(pattern)
indexplain = bytearray(32)
for i,ind in enumerate(cippat):
    indexplain[ind] = cip[i]
printbytes(indexplain)
