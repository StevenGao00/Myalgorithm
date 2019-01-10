#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List
from itertools import accumulate

def min_dist(weight:List[List[int]]) -> int:
    m, n  = len(weight), len(weight[0])
    table = [[0]*n for i in range(m)]
    table[0] = list(accumulate(weight[0]))
    tmp = 0
    for i in range(m):
        tmp += weight[i][0]
        table[i][0] = tmp
    for i in range(1, m):
        for j in range(1, n):
            table[i][j] = weight[i][j] + min(table[i][j-1], table[i-1][j])
    return table[-1][-1]

def min_dist_recur(weight:List[List[int]]) -> int:
    m, n = len(weight), len(weight[0])
    table = [[0]*n for i in range(m)]
    table[0][0] = weight[0][0]
    def minDist(i:int, j:int):
        if i==0 and j==0:
            return weight[0][0]
        if table[i][j]:
            return table[i][j]
        minLeft = float("inf") if j-1 < 0 else minDist(i, j-1)
        minUp = float("inf") if i-1 < 0 else minDist(i-1, j)
        table[i][j] = weight[i][j] + min(minLeft, minUp)
        return table[i][j]
    return minDist(m-1, n-1)

if __name__=="__main__":
    weight = [[1,3,5,9],[2,1,3,4],[5,2,6,7],[6,8,4,3]]
    print(min_dist(weight))
    print(min_dist_recur(weight))