#!/usr/bin/env python3
"""
Author : Johan Runesson <info@johanrunesson.se>
Date   : 2020-08-03
Purpose: Picnic game 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='item',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start things up"""

    args = get_args()
    items = args.item
    sorted = args.sorted
    num = len(items)

    if sorted:
        items.sort()

    if num > 1:
        items.insert(-1, 'and')

    if num > 3:
        last = items.pop();
        items = ', '.join(items) + ' ' + last
    else:
        items = ' '.join(items)

    print(f'You are bringing {items}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
