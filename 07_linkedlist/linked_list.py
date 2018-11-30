#!usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.append('E:/python/06_linkedlist')
from singly_linklist import singlylinklist


def reverse_list(head):
    rever_head = None
    while head:
        head_next = head._next
        head._next = rever_head
        rever_head = head        # 翻转链表，不要忘了幅值
        head = head_next
    return rever_head

def create_cycle_linked_list(List):
    l = singlylinklist()
    for i in List:
        l.insert_value_to_tail(i)
    tmp = head = l._head
    while tmp._next:
        tmp = tmp._next
    slow = fast =  l._head
    while fast:
        slow = slow._next
        fast = fast._next._next
    tmp._next = slow
    # 打印链表
    n = 0
    Str = str(head.data)
    while n<50:
        head = head._next
        Str = Str + '->' + str(head.data)
        n += 1
    print(Str)
    return l

if __name__=='__main__':
    test_str = range(1,21)
    list1 = singlylinklist()
    for i in test_str:
        list1.insert_value_to_tail(i)
    list1.print_all()
    list1._head = reverse_list(list1._head)
    list1.print_all()
    cylcle_list = create_cycle_linked_list(test_str)
