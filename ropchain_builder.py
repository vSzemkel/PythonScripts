
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

f = open("ropchain.bin", "wb")

# build payload

f.close()
