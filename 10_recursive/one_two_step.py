#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
    假如有n个台阶，一次只可以跨1个或2个台阶，请问走这n个台阶有多少种走法？
    解决重复计算，采用数据保存方法
'''

from typing import Optional

def helper(n:int, values:list) -> Optional[int]:
    if values[n] != 0:
        return values[n]
    values[n] = helper(n-1, values) + helper(n-2, values)
    return values[n]
def climbStaris(n: int) -> Optional[int]:
    values = [0]*(n+1)
    if n<=2:
        return n
    values[1], values[2] = 1, 2
    res = helper(n, values)
    return res

# 使用迭代实现递归
def climbStaris_iteration(n:int) -> Optional[int]:
    if n<=2 and n>=0:
        return n
    res:int = 0
    pre_1 = 2
    pre_2 = 1
    for i in range(3, n+1, 1):
        res = pre_1 + pre_2
        pre_2 = pre_1
        pre_1 = res
    return res

if __name__=="__main__":
    print('1  -> %d' % climbStaris(1))
    print('2  -> %d' % climbStaris(2))
    print('3  -> %d' % climbStaris(3))
    print('4  -> %d' % climbStaris(4))
    print('5  -> %d' % climbStaris(5))
    print('6  -> %d' % climbStaris(6))
    print('7  -> %d' % climbStaris(7))
    print('8  -> %d' % climbStaris(8))
    print('9  -> %d' % climbStaris(9))
    print('10 -> %d' % climbStaris(10))

    print('10 -> %d' % climbStaris_iteration(10))
