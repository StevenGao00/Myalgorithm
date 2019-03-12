#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Optional

# 动态规划-最长公共子串
# 时间复杂度O(n^2)，空间复杂度O(n^2)

def maxSubstring_BT(str1:str, str2:str) -> Optional[int]:
    n = len(str1)
    m = len(str2)
    memo = [[-1] * n for _ in range(m)]
    for i in range(m):
        if str1[0] == str2[i]:
            memo[0][i] = 1
        elif i != 0:
            memo[0][i] = memo[0][i-1]
        else:
            memo[0][i] = 0
    for j in range(n):
        if str2[0] == str1[j]:
            memo[j][0] = 1
        elif j != 0:
            memo[j][0] = memo[j-1][0]
        else:
            memo[j][0] = 0
    for i in range(1, n):
        for j in range(1, m):
            if str1[i] == str2[j]:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1], memo[i-1][j-1]+1)
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1], memo[i-1][j-1])
    return memo[-1][-1]

if __name__=='__main__':
    str1 = 'mitcmuty'
    str2 = 'mtacnupy'
    print(maxSubstring_BT(str1, str2))