#!/usr/bin/env bash
# Default settings for dithering

OUT_FILE="assets/images/${1%.*}.png"
PALETTE='#1d2021 #3c3836 #665c54
 #928374 #f9f5d7 #fbf1c7 #f2e5bc #d5c4a1 #a89984
 #fb4934 #b8bb26 #fabd2f #83a598 #d3869b #8ec07c #fe8019 #cc241d
 #98971a #d79921 #458588 #b16286 #689d6a #d65d0e #9d0006 #79740e
 #b57614 #076678 #8f3f71 #427b58 #af3a03'

didder -i $1 -o $OUT_FILE \
--width 500 \
--palette "$PALETTE" \
edm --serpentine FloydSteinberg

FILESIZE=$(stat -c %s $OUT_FILE)
FILESIZE=$(expr $FILESIZE / 1024)
echo "Written to $OUT_FILE (${FILESIZE}K)"

which kitten > /dev/null && kitten icat $OUT_FILE
