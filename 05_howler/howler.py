#!/usr/bin/env python3
"""
Author : Johan Runesson <info@johanrunesson.se>
Date   : 2020-08-04
Purpose: Howler (upper-cases input) 
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start things up"""

    args = get_args()
    text = args.text
    outfile = args.outfile
    output = text.upper()

    # validate arguments inside get_args (see solution1.py)
    if os.path.isfile(text):
        fh_in = open(text)
        output = fh_in.read().upper()
        fh_in.close()

    if outfile:
        fh_out = open(outfile, 'wt')
        fh_out.write(output)
        fh_out.close()
    else:
        print(output)


# --------------------------------------------------
if __name__ == '__main__':
    main()
