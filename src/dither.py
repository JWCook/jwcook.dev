#!/usr/bin/env python
"""Wrapper script to dither images using the didder CLI tool"""

import os
import subprocess
import sys
from argparse import ArgumentParser
from logging import getLogger
from pathlib import Path

from . import ROOT_DIR

logger = getLogger(__name__)

OUTPUT_DIR = ROOT_DIR / 'assets' / 'images'
PALETTE_MONOCHROME = ['#3c3836', '#fabd2f']
PALETTE_4 = ['#3c3836', '#fabd2f', '#d79921', '#928374']
PALETTE_8 = ['#3c3836', '#fabd2f', '#d79921', '#928374', '#83a598', '#d3869b', '#fb4934', '#fe8019']
PALETTE_16 = [
    '#3c3836',
    '#fabd2f',
    '#d79921',
    '#928374',
    '#83a598',
    '#d3869b',
    '#fb4934',
    '#fe8019',
    '#8ec07c',
    '#b8bb26',
    '#d65d0e',
    '#b16286',
    '#cc241d',
    '#98971a',
    '#ebdbb2',
    '#928374',
]
PALETTE_32 = [
    '#1d2021',
    '#504945',
    '#3c3836',
    '#665c54',
    '#928374',
    '#f9f5d7',
    '#fbf1c7',
    '#f2e5bc',
    '#d5c4a1',
    '#a89984',
    '#fb4934',
    '#b8bb26',
    '#fabd2f',
    '#83a598',
    '#d3869b',
    '#8ec07c',
    '#fe8019',
    '#cc241d',
    '#98971a',
    '#d79921',
    '#458588',
    '#b16286',
    '#689d6a',
    '#d65d0e',
    '#9d0006',
    '#79740e',
    '#b57614',
    '#076678',
    '#8f3f71',
    '#427b58',
    '#af3a03',
]
PALETTES = {
    2: PALETTE_MONOCHROME,
    4: PALETTE_4,
    8: PALETTE_8,
    16: PALETTE_16,
    32: PALETTE_32,
}


def main():
    parser = ArgumentParser(description='Process images with dithering.')
    parser.add_argument('input_path', type=str, help='Input file path')
    parser.add_argument(
        '--output-path',
        '-o',
        type=str,
        default=OUTPUT_DIR,
        help='Output file or directory path',
    )
    parser.add_argument(
        '--colors',
        '-c',
        type=int,
        choices=PALETTES.keys(),
        default=32,
        help='Number of colors in the palette',
    )
    parser.add_argument('--width', '-w', type=int, default=256, help='Width of the output image')
    args = parser.parse_args()
    dither(args.input_path, args.output_path, args.colors, args.width)


def dither(input_path: str, output_path: str = OUTPUT_DIR, colors: int = 32, width: int = 256):
    # Determine the palette to use
    if not (palette := PALETTES.get(colors)):
        logger.info(f'Invalid number of colors: {colors}')
        sys.exit(1)

    # Resolve file paths
    input_path = Path(input_path).resolve()
    output_path = Path(output_path).resolve()
    if output_path.is_dir():
        output_path = output_path / f'{input_path.stem}.png'
    output_path.parent.mkdir(exist_ok=True, parents=True)

    didder_command = [
        'didder',
        '-i',
        input_path,
        '-o',
        output_path,
        '--width',
        width,
        '--palette',
        ' '.join(palette),
        '--compression',
        'size',
        'edm',
        '--serpentine',
        'FloydSteinberg',
    ]
    didder_command = [str(i) for i in didder_command]
    logger.debug(f'Running command:\n{" ".join(didder_command)}')

    subprocess.run(didder_command)

    # Show file size
    file_size = os.path.getsize(output_path) // 1024
    logger.info(f'Written to {output_path} ({file_size}K)')

    # Display image if running in kitty terminal
    if os.environ['TERM'] == 'xterm-kitty':
        subprocess.run(['kitten', 'icat', output_path])


if __name__ == '__main__':
    main()
