"""
Generates MD5 hash for provided filepath
"""

import sys
import base64
from hashlib import md5

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filepath>")
    sys.exit(0)

try:
    with open(sys.argv[1], "rb") as file:
        content = file.read()
        hh = md5(content)
        print("    MD5: ", hh.hexdigest().upper())
        print("MD5-B64: ", base64.b64encode(hh.digest()).decode('ascii'))
except FileNotFoundError:
    sys.exit(f"cannot open {sys.argv[1]}")
