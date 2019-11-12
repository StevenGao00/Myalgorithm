#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
    Implementation of DynamicArray and queue based upon linked list in python
'''
from typing import Optional

class Node:
    def __init__(self, data: str, next=None):
        self.data = data
        self._next = next

class LinkedQueue:
    def __init__(self):
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

    def enqueue(self, item: str):
        new_node = Node(item)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        if self._head:
            item = self._head.data
            self._head = self._head._next
            if not self._head:
                self._tail = None
            return item

    def __repr__(self) -> Optional[str]:
        items = []
        current = self._head
        while current:
            items.append(current.data)
            current = current._next
        return '->'.join(item for item in items)

if __name__=="__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)
    for _ in range(5):
        q.dequeue()
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    print(q)