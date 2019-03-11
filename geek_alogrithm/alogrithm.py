#/usr/bin/env python3
# -*- coding: utf-8 -*-

# 翻转单链表
# LeetCode: https://leetcode.com/problems/reverse-linked-list/submissions/
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next    #sequence unpacking
        return prev

#两两交换链表中的节点
#LeetCode:https://leetcode.com/problems/swap-nodes-in-pairs/submissions/
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next
        return  head

#检测链表是否有环
#LeetCode:https://leetcode.com/problems/linked-list-cycle/submissions/
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
# 检测环开始位置
# LeetCode:https://leetcode.com/problems/linked-list-cycle-ii/
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = tmp = head
        while fast and slow and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                while(1):
                    if fast is tmp:
                        return fast
                    fast, tmp = fast.next, tmp.next
        return None

# 括号匹配
def isValid(s:str):
    stack = []
    paren_map = {')':'(', ']':'[', '}':'{'}
    for item in s:
        if item not in paren_map:
            stack.append(item)
        elif not stack or paren_map[item] != stack.pop():
            return False
    return not stack

# 每 k 个节点一组翻转链表
# leetcode: https://leetcode.com/problems/reverse-nodes-in-k-group/submissions/
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dump = jump = ListNode(0)
        dump.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count = count + 1
            cur, pre = l, r
            if count  == k:
                for _ in range(k):
                    cur.next, pre, cur = pre, cur, cur.next  # 运行一次做一次指向，运行k次
                jump.next, jump, l = pre, l, r
            else:
                return dump.next


# 取数组中第k大的数
# leetcode: https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest(object):
    def __init__(self, k, nums):
        """
        :param k:
        :param nums:
        """
        self.arr = nums
        heapq.heapify(self.arr)
        self.k = k
        while len(self.arr) > self.k:
            heapq.heappop(self.arr)
    def add(self, val):
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, val)
        elif val > self.arr[0]:
            heapq.heapreplace(self.arr, val)
        return self.arr[0]

# 取滑动窗口中最大的数
# leetcode: https://leetcode.com/problems/sliding-window-maximum/submissions/
# 解决思路1、建立大顶堆，时间复杂度O(n*logk) 思路2、双端队列，时间复杂度O(n*1)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        window, res = [], []
        for i, val in enumerate(nums):
            if i >= k and i - k >= window[0]:
                window.pop(0)
            while window and nums[window[-1]] <= val:
                window.pop()
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res