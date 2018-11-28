"""
a: reverse singly-linked list
b: detect cycle in the list
c: merge two sorted list
d: remove nth node from tail
e: find middle node
"""
import sys
sys.path.append('D:\\alog\\Myalgorithm\\06_linkedlist')

from typing import  Optional
from singly_linklist import singlylinklist
from singly_linklist import Node

'''
class Node:
    def __init__(self, data: int, next=None):
        self.data = data
        self._next = next
        '''
# reverse singly-linked list
def reverse(head):
    rever_head = None
    while head:
        head_next = head._next
        head._next = rever_head
        rever_head = head        # 翻转链表，不要忘了幅值
        head = head_next
    return rever_head


if __name__=='__main__':
    link_str = range(1,21)
    link1 = singlylinklist()
    for i in link_str:
        link1.insert_value_to_tail(i)
    link1.print_all()
    reverse(link1)

