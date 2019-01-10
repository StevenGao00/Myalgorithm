#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
python中的全局变量的调用和嵌套函数中变量的使用
全局变量调用：想要在自定义的函数中使用全局变量，就得要在
函数用关键字global声明，然后就可以对全局变量进行修改。
嵌套函数中的变量的调用：要在嵌套的变量中，使用nonlocal的声明
"""

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

def coins_bt(values:List[int], target:int) -> int:
    min_number = float("inf")
    def coins_bt_to(values:List[int], target:int, cur_value:int, coins_num:int) -> int:
        if cur_value == target:
            nonlocal min_number
            if coins_num < min_number:
                min_number = coins_num
        else:
            for i in values:
                if cur_value + i <= target:
                    coins_bt_to(values,target,cur_value+i,coins_num+1)
    coins_bt_to(values,target,0,0)
    return min_number

if __name__=="__main__":
    values = [1,3,5]
    target = 23
    print(coins_dp(values, target))
    print(coins_bt(values, target))

