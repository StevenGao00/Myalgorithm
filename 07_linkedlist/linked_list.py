#!usr/bin/python
# -*- coding: utf-8 -*-

import sys
#sys.path.append('D:/alog/Myalgorithm/06_linkedlist')
sys.path.append('E:/python/06_linkedlist')


from singly_linklist import singlylinklist
from singly_linklist import  Node
from typing import Optional


# 翻转链表
def reverse_list(head:Node) -> Optional[Node]:
    rever_head = None
    while head:
        head_next = head._next
        head._next = rever_head
        rever_head = head        # 翻转链表，不要忘了幅值
        head = head_next
    return rever_head

# 检测链表是否有环
def has_cycle(head:Node) -> bool:
    slow, fast = head, head
    while fast and fast._next:    #有可能fast存在，但是fast._next=None，导致fast._next._next报错
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            return True
    return False

# 检测是否有环，若没有，返回None，若有环则返回环入口
def cycle_entrance(head:Node) -> Optional[Node]:
    slow, fast = head, head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            tmp = head
            while tmp != slow:
                tmp = tmp._next
                slow = slow._next
            return slow
    return None


# 创建有环单链表
def create_cycle_linked_list(List):
    l = singlylinklist()
    for i in List:
        l.insert_value_to_tail(i)
    tmp = head = l._head
    while tmp._next:
        tmp = tmp._next
    slow, fast =  l._head, l._head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
    tmp._next = slow
    # 打印链表
    n = 0
    Str = str(head.data)
    while n<32:
        head = head._next
        Str = Str + '->' + str(head.data)
        n += 1
    print(Str)
    return l

# 合并有序链表
def merge_sorted_list(l1:Node,l2:Node)->Optional[Node]:
    if l1 and l2:
        p1, p2 = l1, l2
        fake_head = Node(None)
        current = fake_head
        while p1 and p2:
            if p1.data <= p2.data:
                current._next = p1
                p1 = p1._next
            else:
                current._next = p2
                p2 = p2._next
            current = current._next
        current._next = p1 if p1 else p2
        return fake_head._next
    return l1 or l2


if __name__=='__main__':
    test_str = range(1,21)
    list1 = singlylinklist()
    for i in test_str:
        list1.insert_value_to_tail(i)
    list1.print_all()
    list1._head = reverse_list(list1._head)
    list1.print_all()

    #  生成循环链表，检测环
    cylcle_list = create_cycle_linked_list(test_str)
    has_cycle = has_cycle(cylcle_list._head)
    print('\ncylcle_list has cycle?',has_cycle, '\n')

    # 检测环入口
    for index, Link in enumerate([list1, cylcle_list]):
        cycle_node = cycle_entrance(Link._head)
        if cycle_node:
            print('链表 cylcle_list 环入口是: ' , cycle_node.data+1 ,'\n')
        else:
            print('链表 list1 不存在环!\n')

    # 生成两个链表
    List1 = range(1,10,2)
    List2 = range(1,10,1)
    linklist1 = singlylinklist()
    linklist2 = singlylinklist()
    for i in List1:
        linklist1.insert_value_to_tail(i)
    for i in List2:
        linklist2.insert_value_to_tail(i)

    merge_list = singlylinklist()
    merge_list._head = merge_sorted_list(linklist1._head,linklist2._head)
    merge_list.print_all()


