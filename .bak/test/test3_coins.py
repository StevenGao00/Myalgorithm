#/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List, Optional

def coins_dp(values:List, target:int) -> Optional[List]:
    n = len(values)
    memo = [0] * (target+1)
    memo[0] = 0
    for i in range(1, target+1):
        min_tmp = float("inf")
        for j in range(n):
            if i-values[j]>=0:
                min_tmp = min(min_tmp, 1+memo[i-values[j]])
        memo[i] = min_tmp
    return memo[-1]


if __name__=="__main__":
    # f(9) = 1 + min(f(9-1), f(9-3), f(9-5))
    values = [1,3,5]
    target = 5
    print(coins_dp(values, target))