#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Tuple, Optional

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

def full_reduction(items:List[int], w:int) -> Optional[list]:
    """
    淘宝双十一购物节满减活动比如‘满200￥减50￥’.假设女友购物车有 n 个（n>100）个想买的商品，她希望从中选几个，
    在凑够满减条件下，让选出来的商品价格总和最大程度接近满减条件（200￥）。
    :param items: n 件商品各自的价格
    :param w: 满减条件
    :return: 购买那些商品
    """
    n = len(items)
    memo = [[0]*(3*w+1) for i in range(n)]
    memo[0][0] = 1
    if items[0] <= 3*w:
        memo[0][items[0]] = 1
    for i in range(1, n):
        for j in range(3*w+1):
            if memo[i-1][j] != 0:
                memo[i][j] = memo[i-1][j]
                if items[i]+j <= 3*w:
                    memo[i][items[i]+j] = 1
    tmp = 0
    for j in  range(w, 3*w+1):
        if memo[n-1][j] == 1:
            tmp = j
            break
    if tmp == 0:
        return []
    select:List[int] = []
    for i in range(n-1, 0, -1):
        if (tmp-items[i] >= 0) and (memo[i-1][tmp-items[i]] == 1):
            select.append((i, items[i]))
            tmp = tmp - items[i]
    if tmp > 0:
        select.append((0, items[0]))
    return select

if __name__=="__main__":
    # [weight, ...]
    items_info = [2, 2, 4, 6, 3]
    capacity = 9
    print(bag(items_info, capacity))

    # [(weight, value), ...]
    items_info = [(3, 5), (2, 2), (1, 4), (1, 2), (4, 10)]
    capacity = 8
    print(bag_with_max_value(items_info, capacity))

    # 淘宝双十一购物满减活动
    items:List[int] = [123,88,56,74,89,136,99,211]
    select = full_reduction(items, 200)
    total_price = sum([i[1] for i in select])
    print(select)
    print(total_price)


