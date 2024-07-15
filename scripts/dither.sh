#!/usr/bin/env bash
# Default settings for dithering
# Uses the didder CLI tool: https://github.com/makew0rld/didder
set -e
FILENAME=$(basename "$1")
OUT_FILE="assets/images/${FILENAME%.*}.png"

PALETTE_MONOCHROME="#3c3836 #fabd2f"
PALETTE_4="#3c3836 #fabd2f #d79921 #928374"
PALETTE_8="\
    #3c3836 #fabd2f #d79921 #928374
    #83a598 #d3869b #fb4934 #fe8019"
PALETTE_16="\
    #3c3836 #fabd2f #d79921 #928374
    #83a598 #d3869b #fb4934 #fe8019
    #8ec07c #b8bb26 #d65d0e #b16286
    #cc241d #98971a #ebdbb2 #928374"
PALETTE_32="\
    #1d2021 #504945 #3c3836 #665c54
    #928374 #f9f5d7 #fbf1c7 #f2e5bc
    #d5c4a1 #a89984 #fb4934 #b8bb26
    #fabd2f #83a598 #d3869b #8ec07c
    #fe8019 #cc241d #98971a #d79921
    #458588 #b16286 #689d6a #d65d0e
    #9d0006 #79740e #b57614 #076678
    #8f3f71 #427b58 #af3a03"


# Determine the palette to use
PALETTE=$PALETTE_32
if [ "$2" == "--colors" ]; then
    case "$3" in
        2) PALETTE=$PALETTE_MONOCHROME;;
        4) PALETTE=$PALETTE_4;;
        8) PALETTE=$PALETTE_8;;
        16) PALETTE=$PALETTE_16;;
        32) PALETTE=$PALETTE_32;;
        *) echo "Invalid number of colors: $3" && exit 1;;
    esac
fi
printf "Using palette:\n%s\n" "$PALETTE"

# Process image
didder -i $1 -o $OUT_FILE \
--width 500 \
--palette "$PALETTE" \
edm --serpentine FloydSteinberg

# Show file size
FILESIZE=$(stat -c %s $OUT_FILE)
FILESIZE=$(expr $FILESIZE / 1024)
echo "Written to $OUT_FILE (${FILESIZE}K)"

# Display image in terminal, if possible
which kitten > /dev/null && kitten icat $OUT_FILE
