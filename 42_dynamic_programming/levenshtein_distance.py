#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Optional

#莱文斯坦距离
#回溯法时间复杂度O(3^n), 空间复杂度O(1)
def minDist_BT(str1:str, str2:str) -> int:
    """
    :param str1: 字符串1
    :param str2: 字符串2
    :return:最小编辑距离
    """
    n = len(str1)
    m = len(str2)
    minDist = float('inf')
    def min_Dist(i:int, j:int, dist:int):
        nonlocal minDist, n, m
        if i == n or j == m:
            if i < n: dist += (n-i)
            if j < m: dist += (m-j)
            if dist < minDist: minDist = dist
            return
        if str1[i] == str2[j]:
            min_Dist(i+1, j+1, dist)
        else:
            min_Dist(i+1, j, dist+1)
            min_Dist(i, j+1, dist+1)
            min_Dist(i+1, j+1, dist+1)
    min_Dist(0,0,0)
    return minDist

#动态规划
#时间复杂度O(n^2), 空间复杂度O(n^2)
def minDist_DP(str1:str, str2:str) -> int:
    """
    :param str1:
    :param str2:
    :return:
    """
    n = len(str1)
    m = len(str2)
    memo = [[-1]*m for _ in range(n)]
    # 初始化memo状态矩阵
    for i in range(m):
        if str1[0] == str2[i]:
            memo[0][i] = i
        elif i != 0:
            memo[0][i] = memo[0][i-1] + 1
        else:
            memo[0][i] = 1
    for j in range(n):
        if str2[0] == str1[j]:
            memo[j][0] = j
        elif j != 0:
            memo[j][0] = memo[j-1][0] + 1
        else:
            memo[j][0] = 1
    # 状态转移
    for i in range(1, n):
        for j in range(1, m):
            if str1[i] == str2[j]:
                memo[i][j] = min(memo[i-1][j]+1, memo[i][j-1]+1, memo[i-1][j-1])
            else:
                memo[i][j] = min(memo[i-1][j]+1, memo[i][j-1]+1, memo[i-1][j-1]+1)
    return memo[-1][-1]

if __name__=='__main__':
    str1 = 'mitcmuty'
    str2 = 'mtacnupy'
    print(minDist_BT(str1, str2))
    print(minDist_DP(str1, str2))