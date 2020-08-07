#!/usr/bin/env python3
"""
Author : Johan Runesson <info@johanrunesson.se>
Date   : 2020-08-07
Purpose: Telephone
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='int',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Start things up"""

    args = get_args()
    text = args.text
    random.seed(args.seed)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    num_mutations = round(len(text) * args.mutations)
    indexes = random.sample(range(len(text)), num_mutations)

    for i in indexes:
        new_char = random.choice(alpha.replace(text[i], ''))
        text = text[:i] + new_char + text[i+1:]
        # alpha2 = alpha.replace(text[i], '')
        # text = text[:i] + random.choice(alpha2) + text[i+1:]
         

    print(f'You said: "{args.text}"')
    print(f'I heard : "{text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
