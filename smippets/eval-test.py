
import struct

a = "ABC"

dupa = {"a": "DEF", "v": "74747"}

print eval('bin(127) + a + "D"', dupa)
print eval('bin(127) + a + "D"')

c = compile('print("a"*100'),'<string>','exec')
eval(c)