#!/usr/bin/python
# # -*- coding: utf-8 -*-

from typing import Optional

class Node:
    def __init__(self, data:int, next=None):
        self.data = data
        self._next=next

class singlylinklist:
    def __init__(self):
        self._head=None
    def find_by_value(self, value:int) -> Optional[Node]:
        p = self._head
        while p and p.data!=value:
            p = p._next
        return p
    def find_by_index(self, index:int) -> Optional[Node]:
        p = self._head
        position  = 0
        while p and position!=index:
            p = p._next
            position += 1
        return p

    def insert_value_to_head(self, value:int):
        new_node = Node(value)
        self.insert_node_to_head(new_node)
    def insert_node_to_head(self, new_node:Node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def insert_value_to_tail(self, value:int):
        new_node=Node(value)
        self.insert_node_to_tail(new_node)
    def insert_node_to_tail(self, new_node):
        p = self._head
        while p and p._next:
            p=p._next
        if p:
            p._next = new_node
        else:
            self._head = new_node

    def insert_value_after(self, node:Node, value:int):
        new_node = Node(value)
        self.insert_node_after(ndoe,new_node)
    def insert_node_after(self, node:Node, new_node:Node):
        if not Node or not new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def insert_value_before(self, node:Node, value:int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)
    def insert_node_before(self, node:Node, new_node:Node):
        if not self._head or not node or not new_node:
            return
        if self._head == node:
            return self.insert_node_to_head(new_node)
        before_ndoe = self._head
        while before_ndoe._next and before_ndoe._next!=node:
            before_ndoe = before_ndoe._next
        if not before_ndoe:
            return
        new_node._next = node
        before_ndoe._next = new_node


    def delete_by_node(self, node:Node):
        if not self._head or not node:
            return
        if node._next:
            node.data =node._next.data
            node._next = node._next._next
            return
        before_node = self._head
        while before_node and before_node._next!=node:
            before_node = before_node._next
        if not before_node:
            return
        before_node._next = None

    def delete_by_value(self, value:int):
        if not self._head or not value:
            return
        fake_head = Node(value+1)
        fake_head._next = self._head
        prev, current = fake_head, self._head
        while current:
            if current.data!=value:
                prev._next = current
                prev = prev._next
            current  =current._next
        if prev._next != None:
            prev._next = None
        self._head = fake_head._next     # case when head.data=value

    def __repr__(self) -> str:
        nums = []
        current = self._head
        while current:
            nums.append(current.data)
            current = current._next
        if len(nums)>0:
            return '->'.join(str(num) for num in nums)
        else:
            return ''

    def print_all(self):
        current = self._head
        if current:
            #print(f"{current.data}", end="")
            print(current.data, end="")
            current = current._next
        while current:
            #print(f"->{current.data}", end="")
            print('->'+str(current.data), end="")
            current = current._next
        print("\n", flush=True)

if __name__=="__main__":
    l = singlylinklist()
    for i in range(15):
        l.insert_value_to_head(i)
    node9 = l.find_by_value(9)
    print(node9.data)
    l.insert_value_before(node9, 20)
    l.print_all()
    l.insert_value_before(node9, 16)
    l.print_all()
    l.insert_value_before(node9, 16)
    l.print_all()
    l.delete_by_value(16)
    l.print_all()
    node11 = l.find_by_index(3)
    print(node11.data)
    l.delete_by_node(node11)
    l.print_all()
    l.delete_by_node(l._head)
    l.print_all()
    l.delete_by_value(13)
    l.print_all()
    print('delete by value(13)', l)