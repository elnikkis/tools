#!/usr/bin/python
# coding: utf-8

from __future__ import print_function
import sys
from itertools import groupby


def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description='uniq -cと同じ動作をして、タブ区切りで出力する')
    parser.add_argument('areaedgefile', type=argparse.FileType('r'), default=sys.stdin, nargs='?',
                        help='input file (default:stdin)')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    for k, g in groupby(args.areaedgefile):
        count = sum(1 for group in g)
        print(k.rstrip(), count, sep='\t')
