#!/usr/bin/env python3
"""
Author : Johan Runesson <info@johanrunesson.se>
Date   : 2020-08-04
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Letter(s)')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start things up"""

    args = get_args()
    dictionary = { line[0].lower(): line.rstrip() for line in args.file }
    # dictionary = {}

    # for line in args.file:
    #     dictionary[line[0].lower()] = line.rstrip()

    for letter in args.letter:
        print(dictionary.get(letter.lower(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
