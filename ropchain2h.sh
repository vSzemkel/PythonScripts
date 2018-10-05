#!/bin/bash

# dos2unix chain2cpp.sh

FILENAME=./ropchain.bin
FILESIZE=$(stat -c%s "$FILENAME")
radare2 -q -c "pc $FILESIZE" $FILENAME > "${FILENAME%.*}.h"
