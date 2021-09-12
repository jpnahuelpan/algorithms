#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Juan Pablo Nahuelpán
""""
Data files:   https://algs4.cs.princeton.edu/14analysis/1Kints.txt
              https://algs4.cs.princeton.edu/14analysis/2Kints.txt
              https://algs4.cs.princeton.edu/14analysis/4Kints.txt
              https://algs4.cs.princeton.edu/14analysis/8Kints.txt
              https://algs4.cs.princeton.edu/14analysis/16Kints.txt
              https://algs4.cs.princeton.edu/14analysis/32Kints.txt
              https://algs4.cs.princeton.edu/14analysis/1Mints.txt
"""
import sys
from ReadFileInts import ReadInts, List


class TreeSum():
    def __init__(self, a: List[int]) -> None:
        self._a = a
        self._count = 0

    def count(self) -> int:
        N: int = len(self._a)
        for i in range(0, N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if (self._a[i] + self._a[j] + self._a[k]) == 0:
                        self._count += 1
        return self._count


if __name__ == "__main__":
    a = ReadInts(sys.argv[1])
    tree_sum = TreeSum(a.read())
    print(str(tree_sum.count()))
