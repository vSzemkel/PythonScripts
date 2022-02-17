#!/usr/bin/python

# based on Gynvael's teachings:
# https://www.youtube.com/watch?v=iwRSFlZoSCM

import distorm3

g_chunk_size      = 20
g_rawtext_begin   = 0x400
g_rawtext_end     = 0x74070
g_virttext_offset = 0x1000
g_memory_base     = 0x7FF970650000 + g_virttext_offset
g_filename = r"C:\Windows\System32\kernel32.dll"
g_cpu_mode = distorm3.Decode64Bits
g_rops = {}

def DecodeAsm(ea, codeChunk):
    global g_cpu_mode

    # binascii.hexlify(d)
    disasm = distorm3.Decode(ea, codeChunk, g_cpu_mode)

    gmap = []
    gtxt = ""

    for (addr, _, inst, _) in disasm:
        inst = inst.lower()
        gtxt += "%s\n" % (inst)
        gmap.append((addr,inst))
        if inst.find("ret") != -1:
            break

    return (gmap, gtxt)

last_found_len = 0
d = open(g_filename, "rb").read()
d = d[g_rawtext_begin:g_rawtext_end] # extract .text section

for i in xrange(g_rawtext_end - g_rawtext_begin):
    if last_found_len > 0:
        last_found_len -= 1
        continue

    (gadget_map, gadget_text) = DecodeAsm(g_memory_base + i, d[i:i + g_chunk_size])

    if gadget_text.find("ret") == -1:
        continue

    if gadget_text.find("db") != -1 or gadget_text.find("iret") != -1 or gadget_text.find("retf") != -1:
        continue

    if len(gadget_map) <= 1:
        continue

    if gadget_text in g_rops:
        continue

    g_rops[gadget_text] = True

    print "------> offset: 0x%x" % (i + g_memory_base)
    for k in gadget_map:
        print "0x%x %s" % (k[0], k[1])
        if k[1].find("ret") != -1:
            break

    last_found_len = gadget_map[-1:][0][0] - gadget_map[0][0] + 1
    print ""

# python rop_hunter.py > kernel32.rop
