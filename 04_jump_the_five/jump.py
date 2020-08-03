#!/usr/bin/env python3
"""
Author : Johan Runesson <info@johanrunesson.se>
Date   : 2020-08-03
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number', metavar='str', help='A number')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start things up"""

    args = get_args()
    number = args.number

    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    for char in number:
        print(jumper.get(char, char), end='')
    print() # To get rid of the %-character at the end (not sure why it gets printed)

    # print(number.translate(number.maketrans(jumper)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
