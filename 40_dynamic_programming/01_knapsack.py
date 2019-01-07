#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Tuple

def bag(items_info:List[int], capacity:int) -> int:
    """
    计算能装进背包的物品组合的最大重量

    :param items_info: 每一个物品的重量
    :param capacity: 背包的容量
    :return: 最大装载重量
    """
    # 初始化状态矩阵
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 1
    if items_info[0] <= capacity:
        memo[0][items_info[0]] = 1
    # 状态转移
    for i in range(1, n):
        for j in range(capacity+1):
            if memo[i-1][j] != -1:
                # 不把第i个物品放入背包
                memo[i][j] = memo[i-1][j]
                # 把第i个物品放入背包
                if items_info[i]+j <= capacity:
                    memo[i][j+items_info[i]] = 1
    for i in range(capacity, -1, -1):
        if memo[-1][i] != -1:
            return i

def bag_with_max_value(items_info:List[Tuple[int, int]], capacity:int) -> int:
    """
    计算能装进背包的物品组合的最大价值

    :param items_info: 物品的重量和价值
    :param capacity: 背包容量
    :return: 最大装载价值
    """
    # 初始化状态矩阵
    n = len(items_info)
    memo = [[-1]*(capacity+1) for i in range(n)]
    memo[0][0] = 0
    if items_info[0][0] <= capacity:
        memo[0][items_info[0][0]] = items_info[0][1]
    # 状态转移
    for i in range(1, n):
        for j in range(capacity+1):
            if memo[i-1][j] != -1:
                # 不把第i个物品放入背包
                memo[i][j] = memo[i-1][j]
                # 把第i个物品放入背包
                if items_info[i][0]+j <= capacity:
                    memo[i][j+items_info[i][0]] = max(
                        memo[i][j+items_info[i][0]],
                        memo[i-1][j] + items_info[i][1]
                    )
    return max(memo[-1])


if __name__=="__main__":
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(bag(items_info, capacity))

    # [(weight, value), ...]
    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    capacity = 8
    print(bag_with_max_value(items_info, capacity))


