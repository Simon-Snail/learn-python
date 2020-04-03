#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Simon'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, word!')
    elif len(args) == 2:
        print('Hello, {}!'.format(args[1]))
    else:
        print('Too many ')

if __name__ == '__main__':
    test()

