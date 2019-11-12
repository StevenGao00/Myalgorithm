#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# a stack based upon singly-linked list
'''

from typing import Optional

class Node:
    def __init__(self, data:int ,next=None):
        self.data = data
        self._next = next

class linkedstack:
    def __init__(self):
        self._top:Node = None

    def push(self, value:int):
        new_top = Node(value)
        new_top._next = self._top
        self._top = new_top

    def pop(self) -> Optional[int]:
        if self._top:
            value = self._top.data
            self._top = self._top._next
        return value

    def __repr__(self) -> str:
        current = self._top
        values = []
        while current:
            values.append(current.data)
            current  =current._next
        return  ' '.join(f"{num}" for num in values)

if __name__=='__main__':
    stack1 = linkedstack()
    for i in range(10):
        stack1.push(i)
    print(stack1)

    for _ in range(3):
        stack1.pop()
    print(stack1)

