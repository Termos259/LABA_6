#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    if len(a) < 2 or a[0] != a[1]:
        print("Неверный картеж", file=sys.stderr)
        exit(1)

    count = a.count(a[0])
    b = a[count:]

    print(count)
    print(str(b)[1:-1])
