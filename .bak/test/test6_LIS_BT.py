#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Optional
global max_val
max_val=0

#回溯法求解，枚举所有可能。时间复杂度O(2^n)
def longest_increasing_subsequence(nums:List, res:List, k:int=-1):
    global max_val
    if not nums or k>=len(nums):
        return
    if not res:
        res.append(nums[0])
        if len(res) > max_val: max_val = len(res)
        longest_increasing_subsequence(nums, res[:], k+1)
    else:
        longest_increasing_subsequence(nums, res[:], k+1)
        if nums[k] > res[-1]:
            res.append(nums[k])
            if len(res) > max_val: max_val = len(res)
            longest_increasing_subsequence(nums, res[:], k+1)

if __name__ == '__main__':
    # 要求输入的都是大于0的正整数(可优化至支持任意整数)
    #nums = [2, 9, 3, 6, 5, 1, 7]
    nums = list(range(10, -1, -1))
    longest_increasing_subsequence(nums, [])
    print(max_val)