#/usr/bin/env python3
# -*- coding: utf-8 -*-

# valid anagram
# 有效异位词：两个单词所组成字母相同，只是顺序不同
# leetcode:https://leetcode.com/problems/valid-anagram/description/
# 思路：1、排序，快排O(n*logn). 2、map映射，时间复杂度O(N*1)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {i:s.count(i) for i in set(s)}
        dict2 = {j:t.count(j) for j in set(t)}
        return dict1 ==  dict2
# group_anagram
# leetcode:
# time O(n), space O(n)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for i in strs:
            b = ''.join(sorted(i))
            if b in res:
                res[b] += [i]
            else:
                res[b] = [i]
        return [res[i] for i in res]

# 两数相加
# 1、暴力搜索O(n^2) 2、map、时间O(n),空间O(n)
# leetcode:https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target - num], i]
            lookup[num] = i
        return []

# 3数相加
# 1、暴力搜索O(n^3) 2、map、c = -(a+b) 时间O(n^2),空间O(n)
# 3、先排序再查找O(n^2), 空间O(1)
# leetcode:https://leetcode.com/problems/3sum/description/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

# 4sum
# leetcode:https://leetcode.com/problems/4sum/
# 1、先排序再查找O(n^3), 空间O(1)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in xrange(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in xrange(i+1, len(nums)-2):
                l, r = j+1, len(nums)-1
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s > target: r -= 1
                    elif s < target:l += 1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        while l < r and nums[l+1] == nums[l]: l += 1
                        while l < r and nums[r-1] == nums[r]: r -= 1
                        l += 1; r -= 1
        return res


# 二分查找，有相同字符，返回下标最小的下标:[1,2,2,3],2  返回1，查找不到返回-1
class BinarySearch:
    def getPos(selfself, A:List, val):
        low, high = 0, len(A)-1
        while low <= high:
            mid = (low + high) // 2
            if A[mid] == val:
                while A[mid] == val:
                    mid -= 1
                return mid + 1
            elif A[mid] > val:
                high = mid -1
            else:
                low = mid + 1
        return -1

# 去哪儿网寻找coder题目
# 测试用力：输入：['i am a coder', 'Coder Coder', 'Code'], 3 输出：['Coder Coder', 'i am a coder']
class coder:
    def findCoder(self, A, n):
        res = []
        for i in A:
            b = i.lower()
            if b.count('coder') != 0:
                res.append([b.count('coder'), i])
        res.sort(key=lambda x:x[0], reverse=True)
    return [i[1] for i in res]