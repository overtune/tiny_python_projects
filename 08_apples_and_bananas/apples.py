#!/usr/bin/env python3
"""
Author : Johan Runesson <info@johanrunesson.se>
Date   : 2020-08-04
Purpose: Apples and bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute',
                        metavar='vowel',
                        type=str,
                        choices=list('aeiou'),
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Start things up"""

    args = get_args()
    text = args.text
    vowel = args.vowel

    new_text = text.translate(str.maketrans('aeiouAEIOU', vowel * 5 + vowel.upper() * 5));

    print(new_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
