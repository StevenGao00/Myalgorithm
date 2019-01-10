#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

def coins_dp(values:List[int], target:int) -> int:
    n = len(values)
    memo = [0] * (target+1)
    memo[0] = 0
    for i in range(1, target+1):
        min_num = float("inf")
        for j in range(n):
            if i >= values[j]:
                min_num = min(min_num, memo[i-values[j]]+1)
            else:
                break
        memo[i] = min_num
    return memo[-1]

if __name__=="__main__":
    values = [1,3,5]
    target = 23
    print(coins_dp(values, target))