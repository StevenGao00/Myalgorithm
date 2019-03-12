#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, Optional

#leetcode:https://leetcode.com/problems/longest-increasing-subsequence/
#动态规划，时间复杂度O(n^2),空间复杂度O(n)
def longest_increasing_subsequence(nums:List) -> Optional[int]:
    """
    :param nums: 输入数组
    :return: 返回最长递增子序列长度
    """
    memo = [1] * len(nums)
    res = 0
    for i, val in enumerate(nums):
        res = max(res, memo[i])
        for j in range(i+1, len(nums)):
            if nums[j] > val:
                memo[j] = max(memo[i]+1, memo[j])
    return res

if __name__ == '__main__':
    # 要求输入的都是大于0的正整数(可优化至支持任意整数)
    #nums = [2, 9, 3, 6, 5, 1, 7]
    nums = list(range(10, -1, -1))
    print(longest_increasing_subsequence(nums))